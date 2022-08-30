from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from recipe.models import Recipe
from recipe.serializers import RecipeMealSerializer
from user.serializers import UserRecipeSerializer

from .models import Meal


class MealSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    creator = UserRecipeSerializer()
    breakfast = RecipeMealSerializer(many=True)
    lunch = RecipeMealSerializer(many=True)
    dinner = RecipeMealSerializer(many=True)
    date = serializers.DateField(format="%d/%m/%Y")

    class Meta:
        model = Meal
        fields = (
            "id",
            "creator",
            "date",
            "breakfast",
            "lunch",
            "dinner",
        )
        read_only_fields = ("id", "creator")


class MealCreateSerializer(serializers.ModelSerializer):
    breakfast = serializers.SlugRelatedField(
        many=True, slug_field="id", queryset=Recipe.objects.all()
    )
    lunch = serializers.SlugRelatedField(
        many=True, slug_field="id", queryset=Recipe.objects.all()
    )
    dinner = serializers.SlugRelatedField(
        many=True, slug_field="id", queryset=Recipe.objects.all()
    )
    date = serializers.DateField()
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Meal
        fields = [
            "date",
            "breakfast",
            "lunch",
            "dinner",
            "creator",
        ]

    def validate_date(self, value):
        user = self.context.get("request").user
        if Meal.objects.filter(creator=user.id).exists():
            raise serializers.ValidationError(_("Meal with that date already exists"))
        return value

    def create(self, data):
        breakfast_recipes = data.pop("breakfast")
        lunch_recipes = data.pop("lunch")
        dinner_recipes = data.pop("dinner")
        created_meal = Meal.objects.create(**data)
        created_meal.breakfast.set(breakfast_recipes)
        created_meal.lunch.set(lunch_recipes)
        created_meal.dinner.set(dinner_recipes)
        return created_meal


class MealUpdateSerializer(MealSerializer):
    breakfast = serializers.SlugRelatedField(
        many=True, slug_field="id", queryset=Recipe.objects.all()
    )
    lunch = serializers.SlugRelatedField(
        many=True, slug_field="id", queryset=Recipe.objects.all()
    )
    dinner = serializers.SlugRelatedField(
        many=True, slug_field="id", queryset=Recipe.objects.all()
    )

    def to_representation(self, instance):
        if self.context["request"].method == "PUT":
            serializer = MealSerializer(instance)
            return serializer.data
        return super().to_representation(instance)
