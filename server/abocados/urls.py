from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(("user.urls", "user"), namespace="users")),
    path("", include(("recipe.urls", "recipe"), namespace="recipes")),
    path("", include(("category.urls", "category"), namespace="categories")),
    path("", include(("meal.urls", "meal"), namespace="meals")),
]
