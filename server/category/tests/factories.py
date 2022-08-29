from factory import Faker, Iterator
from factory.django import DjangoModelFactory
from category.constants import CategoryTypes
from category.models import Category


class CategoryFactory(DjangoModelFactory):
    type = Iterator(CategoryTypes)
    picture = Faker("file_path", extension="jpg")
    name = Faker("name")
    description = Faker("sentence")

    class Meta:
        model = Category
