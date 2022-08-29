from django.urls import include, path
from rest_framework import routers
from meal.views import MealViewSet

router = routers.DefaultRouter()
router.register(r"meals", MealViewSet, basename="meals")

urlpatterns = [
    path("", include(router.urls)),
]
