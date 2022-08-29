from django.test import TestCase
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)
import datetime
from django.conf import settings
from utils.test_utils import PATH, API_ACTIONS, make_api_call
from user.tests.factories import UserFactory
from category.tests.factories import CategoryFactory
from recipe.tests.factories import RecipeFactory


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user1 = UserFactory()
        self.user2 = UserFactory()

        self.category1 = CategoryFactory()
        self.category2 = CategoryFactory()
        self.category3 = CategoryFactory()
        self.category4 = CategoryFactory()

    def make_retrieve_recipe_list_call(self, user=None, query_params={}):
        url = PATH.RECIPE
        return make_api_call(
            route=url, user=user, action=API_ACTIONS.GET, query_params=query_params
        )

    def make_retrieve_recipe_call(self, uuid, user=None):
        return make_api_call(
            route=PATH.RECIPE + "%s/" % (uuid), user=user, action=API_ACTIONS.GET
        )

    def make_create_recipe_call(self, data, user=None):
        return make_api_call(
            route=PATH.RECIPE, user=user, action=API_ACTIONS.POST, body=data
        )

    def make_update_recipe_call(self, uuid, data, user=None):
        return make_api_call(
            route=PATH.RECIPE + "%s/" % (uuid),
            user=user,
            action=API_ACTIONS.PUT,
            body=data,
        )

    def make_delete_recipe_call(self, uuid, user=None):
        return make_api_call(
            route=PATH.RECIPE + "%s/" % (uuid), user=user, action=API_ACTIONS.DELETE
        )

    def _get_recipe_request(
        self,
        name=None,
        directions=None,
        rating=None,
        duration=None,
        ingredients=None,
        categories=None,
    ):
        recipe = RecipeFactory.build()
        data = {
            "name": name or recipe.name,
            "directions": directions or recipe.directions,
            "rating": rating or recipe.rating,
            "duration": duration or recipe.duration,
            "ingredients": ingredients or recipe.ingredients,
            "categories": categories or [],
        }
        return data

    def test_create_recipe_ok(self):
        new_recipe = RecipeFactory.build()

        category_list_id = [self.category1.id, self.category2.id, self.category3.id]

        body = self._get_recipe_request(
            name=new_recipe.name,
            directions=new_recipe.directions,
            rating=new_recipe.rating,
            duration=new_recipe.duration,
            ingredients=new_recipe.ingredients,
            categories=category_list_id,
        )
        response = self.make_create_recipe_call(data=body, user=self.user1)

        content = response.content
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(content["name"], new_recipe.name)
        self.assertEqual(content["directions"], new_recipe.directions)
        self.assertEqual(content["ingredients"], new_recipe.ingredients)
        self.assertEqual(content["duration"], new_recipe.duration)
        self.assertEqual(content["rating"], new_recipe.rating)
        self.assertEqual(content["creator"]["id"], self.user1.id)
        self.assertEqual(content["creator"]["username"], self.user1.username)

        response = self.make_retrieve_recipe_call(uuid=content["id"], user=self.user1)

        content = response.content
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIn(content["categories"][0]["id"], category_list_id)
        self.assertIn(content["categories"][1]["id"], category_list_id)
        self.assertIn(content["categories"][2]["id"], category_list_id)

    def test_create_recipe_no_token(self):
        body = self._get_recipe_request()
        response = self.make_create_recipe_call(data=body, user=None)

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_recipe_without_mandatory_fields(self):
        response = self.make_create_recipe_call(data={}, user=self.user1)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["name"][0], "This field is required.")

    def test_create_recipe_with_empty_fields(self):
        body = self._get_recipe_request()
        body["name"] = ""

        response = self.make_create_recipe_call(data=body, user=self.user1)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["name"][0], "This field may not be blank.")

    def test_create_recipe_with_long_name(self):
        body = self._get_recipe_request(name="a" * 100)

        response = self.make_create_recipe_call(data=body, user=self.user1)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["name"][0],
            "Ensure this field has no more than 50 characters.",
        )

    def test_retrieve_recipe_list_ok(self):
        RecipeFactory.create_batch(5)
        response = self.make_retrieve_recipe_list_call(user=self.user1)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 5)

    def test_retrieve_recipe_list_filter_name(self):
        RecipeFactory.create_batch(5)
        RecipeFactory(name="sushi")
        RecipeFactory(name="sushi maki")

        query_param = {"name": "sushi"}
        response = self.make_retrieve_recipe_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 2)

    def test_retrieve_recipe_list_filter_rating(self):
        RecipeFactory.create_batch(3, rating="2")
        RecipeFactory.create_batch(2, rating="4")
        RecipeFactory.create_batch(2, rating="5")

        query_param = {"rating": "4"}
        response = self.make_retrieve_recipe_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 4)
        self.assertGreaterEqual(response.content["results"][0]["rating"], "4")
        self.assertGreaterEqual(response.content["results"][1]["rating"], "4")

    def test_retrieve_recipe_list_filter_duration(self):
        RecipeFactory.create_batch(3, duration="10")
        RecipeFactory.create_batch(2, duration="30")
        RecipeFactory.create_batch(2, duration="50")
        query_param = {"duration": "30"}
        response = self.make_retrieve_recipe_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 5)
        self.assertLessEqual(response.content["results"][0]["duration"], "30")
        self.assertLessEqual(response.content["results"][1]["duration"], "30")

    def test_retrieve_recipe_list_filter_to_from(self):
        RecipeFactory.create_batch(3)
        query_param = {
            "from_date": "2020-05-17",
            "to_date": datetime.datetime(2020, 5, 18).strftime(
                settings.DATETIME_FORMAT
            ),
        }
        response = self.make_retrieve_recipe_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 0)

    def test_retrieve_recipe_list_filter_creator(self):
        RecipeFactory.create_batch(3, creator=self.user1)
        RecipeFactory.create_batch(2, creator=self.user2)
        query_param = {"creator": self.user1.id}
        response = self.make_retrieve_recipe_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 3)
        self.assertEqual(response.content["results"][0]["creator"]["id"], self.user1.id)

        query_param = {"creator": self.user2.id}
        response = self.make_retrieve_recipe_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 2)
        self.assertEqual(response.content["results"][0]["creator"]["id"], self.user2.id)
        self.assertEqual(response.content["results"][1]["creator"]["id"], self.user2.id)

    def test_retrieve_recipe_list_filter_category(self):
        RecipeFactory.create_batch(3)
        recipe1 = RecipeFactory()
        recipe1.categories.add(self.category1)

        query_param = {"category": self.category1.id}
        response = self.make_retrieve_recipe_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 1)
        self.assertEqual(
            response.content["results"][0]["categories"][0]["name"], self.category1.name
        )
        self.assertEqual(
            response.content["results"][0]["categories"][0]["id"], self.category1.id
        )

    def test_retrieve_recipe_list_no_token(self):
        response = self.make_retrieve_recipe_list_call(user=None)

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_retrieve_recipe_by_id_ok(self):
        recipe = RecipeFactory(creator=self.user1)

        response = self.make_retrieve_recipe_call(uuid=recipe.id, user=self.user1)

        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content["name"], recipe.name)
        self.assertEqual(content["directions"], recipe.directions)
        self.assertEqual(content["duration"], recipe.duration)
        self.assertEqual(content["rating"], recipe.rating)
        self.assertEqual(content["creator"]["id"], self.user1.id)
        self.assertEqual(content["creator"]["username"], self.user1.username)
        self.assertEqual(sorted(content["ingredients"]), sorted(recipe.ingredients))

    def test_retrieve_recipe_by_id_no_token(self):
        recipe = RecipeFactory(creator=self.user1)

        response = self.make_retrieve_recipe_call(uuid=recipe.id)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_retrieve_recipe_by_id_other_creator(self):
        recipe_by_other_creator = RecipeFactory(creator=self.user2)

        response = self.make_retrieve_recipe_call(
            uuid=recipe_by_other_creator.id, user=self.user1
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_retrieve_recipe_by_id_not_found(self):
        response = self.make_retrieve_recipe_call(uuid=435345345, user=self.user1)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_update_recipe_ok(self):
        original_recipe = RecipeFactory(creator=self.user1)
        updated_recipe = RecipeFactory.build()
        body = {
            "name": updated_recipe.name,
        }
        response = self.make_update_recipe_call(
            uuid=original_recipe.id, data=body, user=self.user1
        )

        content = response.content
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(content["name"], updated_recipe.name)
        # check that the rest of the fields are not altered
        self.assertEqual(content["rating"], original_recipe.rating)
        self.assertEqual(content["directions"], original_recipe.directions)
        self.assertEqual(content["duration"], original_recipe.duration)
        self.assertEqual(content["creator"]["id"], original_recipe.creator.id)
        self.assertEqual(
            content["creator"]["username"], original_recipe.creator.username
        )
        self.assertEqual(
            sorted(content["ingredients"]), sorted(original_recipe.ingredients)
        )

    def test_update_recipe_categories_ok(self):
        original_recipe = RecipeFactory(creator=self.user1)
        original_recipe.categories.add(self.category1)

        body = {
            "categories": [self.category4.id],
        }
        response = self.make_update_recipe_call(
            uuid=original_recipe.id, data=body, user=self.user1
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["categories"][0]["id"], self.category4.id)

    def test_update_recipe_readonly_fields(self):
        original_recipe = RecipeFactory(creator=self.user1)
        body = {
            "id": 123456,
            "creator": self.user2,
            "created_at": datetime.datetime(2020, 5, 17),
        }
        response = self.make_update_recipe_call(
            uuid=original_recipe.id, data=body, user=self.user1
        )

        content = response.content
        self.assertEqual(response.status_code, HTTP_200_OK)
        # check that fields are not updated
        self.assertEqual(content["id"], original_recipe.id)
        self.assertEqual(content["creator"]["id"], original_recipe.creator.id)
        self.assertEqual(
            content["creator"]["username"], original_recipe.creator.username
        )
        self.assertEqual(
            content["created_at"],
            original_recipe.created_at.strftime(settings.DATETIME_FORMAT),
        )

    def test_update_recipe_no_token(self):
        recipe = RecipeFactory(creator=self.user1)
        response = self.make_update_recipe_call(
            uuid=recipe.id,
            data={},
        )
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_update_recipe_other_user(self):
        user1_recipe = RecipeFactory(creator=self.user1)

        response = self.make_update_recipe_call(
            uuid=user1_recipe.id, data={}, user=self.user2
        )

        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_update_recipe_inexistent(self):
        response = self.make_update_recipe_call(
            uuid=4534534534, data={}, user=self.user1
        )

        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_recipe_no_token(self):
        recipe = RecipeFactory()
        response = self.make_delete_recipe_call(
            uuid=recipe.id,
        )
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_delete_recipe_other_creator(self):
        user2_recipe = RecipeFactory(creator=self.user2)
        response = self.make_delete_recipe_call(uuid=user2_recipe.id, user=self.user1)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_delete_recipe_not_found(self):
        response = self.make_delete_recipe_call(uuid=345345345, user=self.user1)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_recipe_ok(self):
        recipe_to_delete = RecipeFactory(creator=self.user1)
        response = self.make_delete_recipe_call(
            uuid=recipe_to_delete.id, user=self.user1
        )
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

        response = self.make_delete_recipe_call(
            uuid=recipe_to_delete.id, user=self.user1
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
