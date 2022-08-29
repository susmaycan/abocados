from django.urls import include, path
from user.views import (
    UserViewSet,
    AuthViewSet,
    UserRecipesViewSet,
    UserFavouriteRecipesViewSet,
)
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r"auth", AuthViewSet, basename="auth")
router.register(r"users", UserViewSet, basename="users")

user_recipe_router = routers.NestedSimpleRouter(router, r"users", lookup="user")

user_recipe_router.register(r"recipes", UserRecipesViewSet, basename="user-recipes")

user_recipe_router.register(
    r"favourites", UserFavouriteRecipesViewSet, basename="user-favourite-recipes"
)


urlpatterns = [
    path("", include(router.urls)),
    path("", include(user_recipe_router.urls)),
]
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')
# router.register(r'auth', AuthViewSet, basename='auth')

# favourite_recipe_router = routers.NestedSimpleRouter(router, 'users', lookup='user')
# favourite_recipe_router.register('favourite', RecipeFavouriteViewSet, basename='favourites')

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('', include(favourite_recipe_router.urls)),
# ]
