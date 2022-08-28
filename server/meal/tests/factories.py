from factory import Faker, SubFactory, post_generation
from factory.django import DjangoModelFactory
from meal.models import Meal
from user.tests.factories import UserFactory
from recipe.tests.factories import RecipeFactory


class MealFactory(DjangoModelFactory):
    creator = SubFactory(UserFactory)
    date = Faker('date')

    class Meta:
        model = Meal

    @post_generation
    def add_recipes(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for recipe in extracted:
                self.breakfast.add(recipe)
                self.lunch.add(recipe)
                self.dinner.add(recipe)
        else:
            recipes = RecipeFactory.create_batch(2)
            self.breakfast.set(recipes)
            self.lunch.set(recipes)
            self.dinner.set(recipes)
