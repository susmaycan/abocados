from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from recipe.models import Recipe
from user.tests.factories import UserFactory


class RecipeFactory(DjangoModelFactory):
    name = Faker("name")
    rating = Faker("numerify")
    ingredients = Faker("sentence")
    directions = Faker("sentence")
    picture = Faker("file_path", extension="jpg")
    duration = Faker("numerify")
    servings = Faker("numerify")
    creator = SubFactory(UserFactory)

    class Meta:
        model = Recipe
