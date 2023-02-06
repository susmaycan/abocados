from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from category.models import Category
from category.serializers import CategorySelectSerializer
from user.serializers import UserRecipeSerializer

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    categories = CategorySelectSerializer(many=True)
    creator = UserRecipeSerializer()
    favourited = SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "rating",
            "ingredients",
            "picture",
            "directions",
            "duration",
            "servings",
            "created_at",
            "creator",
            "categories",
            "favourited",
        )
        read_only_fields = ("id", "created_at", "creator")

    def get_favourited(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        return user and user.saved_recipes.filter(id=obj.id).exists()


class RecipeCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    rating = serializers.CharField(max_length=5, required=False)
    duration = serializers.CharField(max_length=10, required=False)
    servings = serializers.CharField(max_length=10, required=False)
    directions = serializers.CharField(max_length=2000, required=False)
    ingredients = serializers.CharField(max_length=2000, required=False)
    picture = serializers.FileField(required=False)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    categories = serializers.SlugRelatedField(
        many=True, slug_field="id", queryset=Category.objects.all()
    )

    class Meta:
        model = Recipe
        fields = [
            "name",
            "rating",
            "duration",
            "directions",
            "picture",
            "ingredients",
            "creator",
            "categories",
            "servings",
        ]

    def create(self, data):
        category_list = data.pop("categories")
        created_recipe = Recipe.objects.create(**data)
        created_recipe.categories.set(category_list)
        return created_recipe


class RecipeUpdateSerializer(RecipeSerializer):
    categories = serializers.SlugRelatedField(
        many=True, slug_field="id", queryset=Category.objects.all()
    )

    def to_representation(self, instance):
        if self.context["request"].method == "PUT":
            serializer = RecipeSerializer(instance)
            return serializer.data
        return super().to_representation(instance)


class RecipeMealSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    creator = UserRecipeSerializer()

    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "rating",
            "picture",
            "duration",
            "servings",
            "creator",
        )
        read_only_fields = ("id", "creator")
