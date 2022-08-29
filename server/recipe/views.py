from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from recipe.filters import RecipeFilter
from recipe.models import Recipe
from recipe.permissions import IsCreator
from recipe.serializers import (RecipeCreateSerializer, RecipeSerializer,
                                RecipeUpdateSerializer)
from user.permissions import IsStandardUser
from utils.constants import RestFrameworkActions
from utils.mixins import EnablePartialUpdateMixin
from utils.pagination import BasePagination


class RecipeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    EnablePartialUpdateMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    filter_class = RecipeFilter
    queryset = Recipe.objects.all().order_by("-created_at")
    pagination_class = BasePagination

    def get_serializer_class(self):
        if self.action in [
            RestFrameworkActions.PARTIAL_UPDATE,
            RestFrameworkActions.UPDATE,
        ]:
            return RecipeUpdateSerializer
        return RecipeSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        if self.action in [
            RestFrameworkActions.UPDATE,
            RestFrameworkActions.PARTIAL_UPDATE,
            RestFrameworkActions.DESTROY,
        ]:
            permission_classes.append(IsCreator)

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = RecipeCreateSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        saved_recipe = serializer.save()
        data = RecipeSerializer(saved_recipe).data
        return Response(data, status=status.HTTP_201_CREATED)
