
from rest_framework.permissions import BasePermission
from recipe.models import Recipe


class IsCreator(BasePermission):
    def has_permission(self, request, view):
        try:
            recipe_id = request.resolver_match.kwargs.get('pk')
            recipe = Recipe.objects.get(id=recipe_id)
            if recipe is None or recipe.creator.id != request.user.id:
                return False
        except Recipe.DoesNotExist:
            # it returns true because 404 error must be thrown
            return True
        return True
