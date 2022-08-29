from django.urls import include, path
from rest_framework import routers
from category.views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")

urlpatterns = [
    path("", include(router.urls)),
]
