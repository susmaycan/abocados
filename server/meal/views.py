from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from meal.filters import MealFilter
from meal.models import Meal
from meal.serializers import (MealCreateSerializer, MealSerializer,
                              MealUpdateSerializer)
from user.permissions import IsStandardUser
from utils.constants import RestFrameworkActions
from utils.mixins import EnablePartialUpdateMixin
from utils.pagination import BasePagination


class MealViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    EnablePartialUpdateMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Meal.objects.all()
    pagination_class = BasePagination
    filter_class = MealFilter

    def get_serializer_class(self):
        if self.action in [
            RestFrameworkActions.PARTIAL_UPDATE,
            RestFrameworkActions.UPDATE,
        ]:
            return MealUpdateSerializer
        return MealSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        return Meal.objects.filter(creator=user).order_by("date")

    def create(self, request, *args, **kwargs):
        serializer = MealCreateSerializer(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        saved_meal = serializer.save()
        data = MealSerializer(saved_meal).data
        return Response(data, status=status.HTTP_201_CREATED)
