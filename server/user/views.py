from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import (
    ListModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from user.serializers import (
    AuthenticatedUserSerializer,
    UserLoginSerializer,
    UserSerializer,
    UserSignUpSerializer,
    UserRetrieveSerializer,
    ResetPasswordEmailRequestSerializer,
    ActivateAccountSerializer,
    PasswordRecoveryCheckSerializer,
    PasswordRecoveryConfirmSerializer,
    FavouriteRecipeSerializer,
)
from user.models import User
from user.permissions import IsStandardUser, IsOwnUser, IsOwnUserNested
from utils.constants import RestFrameworkActions
from utils.mixins import EnablePartialUpdateMixin
from utils.email import EmailUtils
from django.template.loader import get_template
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.tokens import (
    default_token_generator,
    PasswordResetTokenGenerator,
)
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer
from rest_framework.exceptions import NotFound
from utils.pagination import BasePagination
from user.filters import UserRecipesFilter


def send_validation_email(user):
    confirmation_token = default_token_generator.make_token(user)
    encoded_user_id = urlsafe_base64_encode(force_bytes(user.id))

    redirect_url = f"{settings.FRONT_END_URL}activate?user={encoded_user_id}&token={confirmation_token}"

    template = get_template("validate_email.html").render(
        {"username": user.username, "redirect_url": redirect_url}
    )
    EmailUtils.send(subject=_("register Abocados"), template=template, to=[user.email])


def send_password_reset_email(user):
    reset_token = PasswordResetTokenGenerator().make_token(user)
    encoded_user_id = urlsafe_base64_encode(force_bytes(user.id))

    redirect_url = f"{settings.FRONT_END_URL}password/update?user={encoded_user_id}&token={reset_token}"

    template = get_template("recover_password_email.html").render(
        {"username": user.username, "redirect_url": redirect_url}
    )
    EmailUtils.send(
        subject=_("Reset Password Abocados"), template=template, to=[user.email]
    )


class AuthViewSet(GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == RestFrameworkActions.AUTHENTICATED:
            permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {"user": UserSerializer(user).data, "access_token": token}
        return Response(data, status=HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_active = False
        user.save()
        data = UserSerializer(user).data

        send_validation_email(user)

        return Response(data, status=HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def request_validation_email(self, request):
        user_id = request.data.get("id", None)

        try:
            user = User.objects.get(id=user_id)

            # User is already active
            if user.is_active:
                return Response(
                    _("Email is already verified"), status=HTTP_400_BAD_REQUEST
                )

            send_validation_email(user)
            return Response(_("Validation email sent"), status=HTTP_200_OK)
        except User.DoesNotExist:
            return Response(_("Not found"), status=HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"])
    def activate_account(self, request):
        serializer = ActivateAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token, user = serializer.save()

        # Token is invalid
        if not default_token_generator.check_token(user, token):
            return Response(
                _("Token is invalid or expired"), status=HTTP_400_BAD_REQUEST
            )

        user.is_active = True
        user.save()
        return Response(_("Email successfully confirmed"), status=HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def authenticated(self, request):
        data = AuthenticatedUserSerializer(request.user).data
        return Response(data, status=HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def password_recovery_request(self, request):
        serializer = ResetPasswordEmailRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_password_reset_email(user)
        return Response(_("Reset password email sent"), status=HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def password_recovery_check(self, request):
        serializer = PasswordRecoveryCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token, user = serializer.save()

        # Token is invalid
        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response(
                _("Token is invalid or expired"), status=HTTP_400_BAD_REQUEST
            )

        return Response(_("Password token valid"), status=HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def password_recovery_confirm(self, request):
        serializer = PasswordRecoveryConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        user = data["user"]
        password = data["password"]
        token = data["token"]

        # Token is invalid
        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response(
                _("Token is invalid or expired"), status=HTTP_400_BAD_REQUEST
            )

        if not user.is_active:
            user.is_active = True

        user.set_password(password)
        user.save()
        return Response(_("Password changed"), status=HTTP_200_OK)


class UserViewSet(
    GenericViewSet,
    EnablePartialUpdateMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
):
    queryset = User.objects.filter(is_active=True)
    boo = 4

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        if self.action in [
            RestFrameworkActions.UPDATE,
            RestFrameworkActions.PARTIAL_UPDATE,
            RestFrameworkActions.DESTROY,
        ]:
            permission_classes.append(IsOwnUser)
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in [RestFrameworkActions.RETRIEVE]:
            return UserRetrieveSerializer
        return UserSerializer


class UserRecipesViewSet(ListModelMixin, GenericViewSet):
    queryset = Recipe.objects.all().order_by("-created_at")
    pagination_class = BasePagination
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, IsStandardUser, IsOwnUserNested]
    filter_class = UserRecipesFilter

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get("user_pk")
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("User doesnt exist")
        user_recipes = self.queryset.filter(creator=user)
        return user_recipes.order_by("-created_at")


class UserFavouriteRecipesViewSet(ListModelMixin, GenericViewSet):
    queryset = Recipe.objects.all().order_by("-created_at")
    pagination_class = BasePagination
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, IsStandardUser, IsOwnUserNested]

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get("user_pk")
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound(_("User doesnt exist"))
        return user.saved_recipes.all()

    @action(detail=False, methods=["post"])
    def add(self, request, *args, **kwargs):
        serializer = FavouriteRecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recipe = serializer.save()
        user = request.user
        if recipe.creator.id == user.id:
            return Response(
                _("Recipe cannot be created by user"), status=HTTP_400_BAD_REQUEST
            )

        if user.saved_recipes.filter(id=recipe.id).exists():
            return Response(
                _("Recipe is already favourited"), status=HTTP_400_BAD_REQUEST
            )

        request.user.saved_recipes.add(recipe)
        return Response({}, status=HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def delete(self, request, *args, **kwargs):
        serializer = FavouriteRecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recipe = serializer.save()
        user = request.user

        if not user.saved_recipes.filter(id=recipe.id).exists():
            return Response(_("Recipe is not favourited"), status=HTTP_400_BAD_REQUEST)

        request.user.saved_recipes.remove(recipe)
        return Response({}, status=HTTP_200_OK)
