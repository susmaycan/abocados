from factory import Faker, PostGenerationMethodCall
from factory.django import DjangoModelFactory
from user.models import User


class UserFactory(DjangoModelFactory):
    email = Faker("email")
    name = Faker("name")
    username = Faker("name")
    picture = Faker("file_path", extension="jpg")
    password = PostGenerationMethodCall("set_password", "defaultpassword")

    class Meta:
        model = User
