from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from user.permissions import IsStandardUser

from category.serializers import CategorySerializer, CategoryCreateSerializer
from category.models import Category

from utils.constants import RestFrameworkActions
from utils.mixins import EnablePartialUpdateMixin
from utils.pagination import LargePagination


class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    EnablePartialUpdateMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("type")
    pagination_class = LargePagination

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        if self.action in [
            RestFrameworkActions.UPDATE,
            RestFrameworkActions.PARTIAL_UPDATE,
            RestFrameworkActions.DESTROY,
            RestFrameworkActions.CREATE,
        ]:
            permission_classes.append(IsAdminUser)

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = CategoryCreateSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        saved_category = serializer.save()
        data = CategorySerializer(saved_category).data
        return Response(data, status=status.HTTP_201_CREATED)
