from django.test import TestCase
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from category.tests.factories import CategoryFactory
from utils.test_utils import PATH, API_ACTIONS, make_api_call
from user.tests.factories import UserFactory
from recipe.tests.factories import RecipeFactory


class UserRecipesTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user2 = UserFactory()

    def make_retrieve_recipes_of_user_call(self, uuid, user=None, query_params={}):
        return make_api_call(
            route=PATH.USER + "%s" % (uuid) + PATH.RECIPE,
            action=API_ACTIONS.GET,
            user=user,
            query_params=query_params,
        )

    def test_get_user_recipes__ok(self):
        RecipeFactory.create_batch(5, creator=self.user)
        RecipeFactory.create_batch(6, creator=self.user2)

        response = self.make_retrieve_recipes_of_user_call(
            user=self.user, uuid=self.user.id
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content["count"], 5)

        response = self.make_retrieve_recipes_of_user_call(
            user=self.user2, uuid=self.user2.id
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content["count"], 6)

    def test_get_user_recipes__other_user_forbidden(self):

        RecipeFactory.create_batch(5, creator=self.user)
        RecipeFactory.create_batch(6, creator=self.user2)

        response = self.make_retrieve_recipes_of_user_call(
            user=self.user2, uuid=self.user.id
        )
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

        response = self.make_retrieve_recipes_of_user_call(
            user=self.user, uuid=self.user2.id
        )
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_get_user_recipes__no_token(self):
        RecipeFactory.create_batch(5, creator=self.user)
        response = self.make_retrieve_recipes_of_user_call(user=None, uuid=self.user.id)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_get_user_recipes__filter_name(self):
        RecipeFactory.create_batch(2, name="sushi", creator=self.user)
        RecipeFactory.create_batch(7, name="other", creator=self.user)

        query_params = {"name": "sushi"}
        response = self.make_retrieve_recipes_of_user_call(
            user=self.user, uuid=self.user.id, query_params=query_params
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content["count"], 2)

    def test_get_user_recipes__filter_rating(self):
        RecipeFactory.create_batch(3, rating="2", creator=self.user)
        RecipeFactory.create_batch(2, rating="4", creator=self.user)
        RecipeFactory.create_batch(2, rating="5", creator=self.user)

        query_param = {"rating": "4"}
        response = self.make_retrieve_recipes_of_user_call(
            user=self.user, uuid=self.user.id, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 4)
        self.assertGreaterEqual(response.content["results"][0]["rating"], "4")
        self.assertGreaterEqual(response.content["results"][1]["rating"], "4")

    def test_get_user_recipes__filter_duration(self):
        RecipeFactory.create_batch(3, duration="10", creator=self.user)
        RecipeFactory.create_batch(2, duration="30", creator=self.user)
        RecipeFactory.create_batch(2, duration="50", creator=self.user)
        query_param = {"duration": "30"}
        response = self.make_retrieve_recipes_of_user_call(
            user=self.user, uuid=self.user.id, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 5)
        self.assertLessEqual(response.content["results"][0]["duration"], "30")
        self.assertLessEqual(response.content["results"][1]["duration"], "30")

    def test_get_user_recipes__filter_category(self):
        RecipeFactory.create_batch(3, creator=self.user)
        recipe = RecipeFactory(creator=self.user)
        category = CategoryFactory()
        recipe.categories.add(category)

        query_param = {"category": category.id}
        response = self.make_retrieve_recipes_of_user_call(
            user=self.user, uuid=self.user.id, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 1)
        self.assertEqual(
            response.content["results"][0]["categories"][0]["name"], category.name
        )
        self.assertEqual(
            response.content["results"][0]["categories"][0]["id"], category.id
        )
