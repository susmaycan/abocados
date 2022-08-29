from django.contrib.auth import password_validation, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from recipe.models import Recipe
from user.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import DjangoUnicodeDecodeError
from django.http import Http404


class UserRecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )
        read_only_fields = (
            "id",
            "username",
        )


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "name",
            "picture",
        )
        read_only_fields = ("id", "username", "modified")


class AuthenticatedUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "name", "picture", "saved_recipes")
        read_only_fields = ("id", "username", "modified")


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError(_("Invalid credentials"))
        self.context["user"] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context["user"], token.key


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        password = data["password"]
        password_validation.validate_password(password)
        return data

    def create(self, data):
        user = User.objects.create_user(**data)
        return user


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "name",
            "picture",
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=180, required=False)
    picture = serializers.FileField(
        allow_empty_file=True, allow_null=True, required=False
    )
    email = serializers.EmailField(
        required=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def validate(self, data):
        new_data = data
        if "picture" not in new_data:
            new_data["picture"] = ""
        return new_data

    class Meta:
        model = User
        fields = (
            "email",
            "name",
            "picture",
        )


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=5)

    class Meta:
        fields = ["email"]

    def validate(self, data):
        try:
            email = data.get("email", "")
            if not User.objects.filter(email=email).exists():
                raise serializers.ValidationError(_("Email not registered"))
            return data
        except User.DoesNotExist:
            raise serializers.ValidationError(_("Email not registered"))

    def create(self, data):
        email = data.get("email", "")
        return User.objects.get(email=email)


class ActivateAccountSerializer(serializers.Serializer):
    token = serializers.CharField(required=False)
    user = serializers.CharField(required=False)

    class Meta:
        fields = ["token", "user"]

    def validate(self, data):
        new_data = data
        try:
            user = data.get("user", "")
            token = data.get("token", "")

            if not user or not token:
                raise serializers.ValidationError(_("Token is invalid or expired"))

            user_id = int(urlsafe_base64_decode(user).decode())
            user_obj = User.objects.get(id=user_id)
            new_data["user"] = user_obj
            if user_obj.is_active:
                raise serializers.ValidationError(_("Email has already been verified"))
            return new_data
        except (
            UnicodeDecodeError,
            DjangoUnicodeDecodeError,
            User.DoesNotExist,
            ValueError,
        ):
            raise serializers.ValidationError(_("Token is invalid or expired"))

    def create(self, data):
        user = data.get("user", "")
        token = data.get("token", "")
        return token, user


class PasswordRecoveryCheckSerializer(serializers.Serializer):
    token = serializers.CharField(required=False)
    user = serializers.CharField(required=False)

    class Meta:
        fields = ["token", "user"]

    def validate(self, data):
        new_data = data
        try:
            user = data.get("user", "")
            token = data.get("token", "")

            if not user or not token:
                raise serializers.ValidationError(_("Token is invalid or expired"))

            if len(user) % 4 == 1:
                raise serializers.ValidationError(_("Token is invalid or expired"))

            user_id = urlsafe_base64_decode(user).decode()
            user_obj = User.objects.get(id=user_id)
            new_data["user"] = user_obj
            return new_data
        except (UnicodeDecodeError, DjangoUnicodeDecodeError):
            raise serializers.ValidationError(_("Token is invalid or expired"))
        except (User.DoesNotExist):
            raise serializers.ValidationError(_("Email not registered"))

    def create(self, data):
        user = data.get("user", "")
        token = data.get("token", "")
        return token, user


class PasswordRecoveryConfirmSerializer(serializers.Serializer):
    token = serializers.CharField(required=False)
    user = serializers.CharField(required=False)
    password = serializers.CharField(min_length=8, max_length=64)

    class Meta:
        fields = ["token", "user", "password"]

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate(self, data):
        new_data = data
        try:
            user = data.get("user", "")
            token = data.get("token", "")

            if not user or not token:
                raise serializers.ValidationError(_("Token is invalid or expired"))

            user_id = urlsafe_base64_decode(user).decode()
            user_obj = User.objects.get(id=user_id)
            new_data["user"] = user_obj
            return new_data
        except (UnicodeDecodeError, DjangoUnicodeDecodeError):
            raise serializers.ValidationError(_("Token is invalid or expired"))
        except (User.DoesNotExist):
            raise serializers.ValidationError(_("Email not registered"))

    def create(self, data):
        return data


class FavouriteRecipeSerializer(serializers.Serializer):
    recipe = serializers.CharField(required=True)

    class Meta:
        fields = ["recipe"]

    def validate_recipe(self, value):
        try:
            recipe_obj = Recipe.objects.filter(id=value)
            if not recipe_obj.exists():
                raise Http404
            return value
        except Recipe.DoesNotExist:
            raise Http404

    def create(self, data):
        return Recipe.objects.get(id=data["recipe"])
