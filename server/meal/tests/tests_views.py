from django.test import TestCase
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND)

from meal.tests.factories import MealFactory
from recipe.tests.factories import RecipeFactory
from user.tests.factories import UserFactory
from utils.test_utils import API_ACTIONS, PATH, format_date, make_api_call


class MealTestCase(TestCase):
    def setUp(self):
        self.user1 = UserFactory()
        self.user2 = UserFactory()

    def make_retrieve_meal_list_call(self, user=None, query_params={}):
        url = PATH.MEAL
        return make_api_call(
            route=url, user=user, action=API_ACTIONS.GET, query_params=query_params
        )

    def make_retrieve_meal_call(self, uuid, user=None):
        return make_api_call(
            route=PATH.MEAL + "%s/" % (uuid), user=user, action=API_ACTIONS.GET
        )

    def make_create_meal_call(self, data, user=None):
        return make_api_call(
            route=PATH.MEAL, user=user, action=API_ACTIONS.POST, body=data
        )

    def make_update_meal_call(self, uuid, data, user=None):
        return make_api_call(
            route=PATH.MEAL + "%s/" % (uuid),
            user=user,
            action=API_ACTIONS.PUT,
            body=data,
        )

    def make_delete_meal_call(self, uuid, user=None):
        return make_api_call(
            route=PATH.MEAL + "%s/" % (uuid), user=user, action=API_ACTIONS.DELETE
        )

    def _get_meal_request(self, date=None, breakfast=None, lunch=None, dinner=None):
        meal = MealFactory.build()
        data = {
            "date": date or meal.date,
            "breakfast": breakfast or [],
            "lunch": lunch or [],
            "dinner": dinner or [],
        }
        return data

    def test_retrieve_meal_list_ok(self):
        MealFactory.create_batch(5, creator=self.user1)
        MealFactory.create_batch(8, creator=self.user2)

        response = self.make_retrieve_meal_list_call(user=self.user1)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 5)

        response = self.make_retrieve_meal_list_call(user=self.user2)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 8)

    def test_retrieve_meal_list_no_token(self):
        MealFactory.create_batch(5, creator=self.user1)
        response = self.make_retrieve_meal_list_call(user=None)

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_retrieve_meal_list_filter_date(self):
        date = "2022-10-22"
        MealFactory.create_batch(3, date=date, creator=self.user1)
        MealFactory.create_batch(2, date="2023-10-22")
        query_param = {"date": date}
        response = self.make_retrieve_meal_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 3)
        self.assertEqual(response.content["results"][0]["date"], format_date(date))

    def test_retrieve_meal_list_filter_to_from(self):
        MealFactory.create_batch(3, date="2022-05-19", creator=self.user1)
        MealFactory.create_batch(3, date="2023-05-19", creator=self.user1)
        query_param = {
            "from_date": "2022-05-17",
            "to_date": "2022-06-17",
        }
        response = self.make_retrieve_meal_list_call(
            user=self.user1, query_params=query_param
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 3)

    def test_retrieve_meal_by_id_ok(self):
        meal = MealFactory(creator=self.user1)
        response = self.make_retrieve_meal_call(user=self.user1, uuid=meal.id)
        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content["creator"]["id"], self.user1.id)
        self.assertEqual(content["date"], format_date(meal.date))
        self.assertEqual(len(content["breakfast"]), len(meal.breakfast.all()))
        self.assertEqual(len(content["lunch"]), len(meal.lunch.all()))
        self.assertEqual(len(content["dinner"]), len(meal.dinner.all()))

    def test_retrieve_meal_by_id_no_token(self):
        meal = MealFactory(creator=self.user1)

        response = self.make_retrieve_meal_call(user=None, uuid=meal.id)

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_meal_ok(self):
        new_meal = MealFactory.build()
        breakfast_recipe = RecipeFactory()
        lunch_recipe_1 = RecipeFactory()
        lunch_recipe_2 = RecipeFactory()
        dinner_recipe = RecipeFactory()

        body = self._get_meal_request(
            date=new_meal.date,
            breakfast=[breakfast_recipe.id],
            lunch=[lunch_recipe_1.id, lunch_recipe_2.id],
            dinner=[dinner_recipe.id],
        )
        response = self.make_create_meal_call(data=body, user=self.user1)

        content = response.content
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(content["breakfast"][0]["id"], breakfast_recipe.id)
        self.assertEqual(content["lunch"][0]["id"], lunch_recipe_1.id)
        self.assertEqual(content["lunch"][1]["id"], lunch_recipe_2.id)
        self.assertEqual(content["dinner"][0]["id"], dinner_recipe.id)
        self.assertEqual(content["date"], format_date(new_meal.date))
        self.assertEqual(content["creator"]["id"], self.user1.id)

        response = self.make_retrieve_meal_call(uuid=content["id"], user=self.user1)

        content = response.content
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_create_meal_no_token(self):
        body = self._get_meal_request()
        response = self.make_create_meal_call(data=body, user=None)

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_meal_without_mandatory_fields(self):
        response = self.make_create_meal_call(data={}, user=self.user1)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["date"][0], "This field is required.")

    def test_create_meal_with_empty_fields(self):
        body = self._get_meal_request()
        body["date"] = ""

        response = self.make_create_meal_call(data=body, user=self.user1)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["date"][0],
            "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
        )

    def test_create_meal_with_wrong_date_format(self):
        body = self._get_meal_request()
        body["date"] = "2002/22/09"

        response = self.make_create_meal_call(data=body, user=self.user1)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["date"][0],
            "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
        )

    def test_update_meal_ok(self):
        original_meal = MealFactory(creator=self.user1)
        updated_meal = MealFactory.build()
        body = {
            "date": updated_meal.date,
        }
        response = self.make_update_meal_call(
            uuid=original_meal.id, data=body, user=self.user1
        )
        content = response.content
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(content["date"], format_date(updated_meal.date))
        # check that the rest of the fields are not altered
        self.assertEqual(len(content["breakfast"]), len(original_meal.breakfast.all()))
        self.assertEqual(len(content["lunch"]), len(original_meal.lunch.all()))
        self.assertEqual(len(content["dinner"]), len(original_meal.dinner.all()))
        self.assertEqual(content["creator"]["id"], original_meal.creator.id)
        self.assertEqual(content["creator"]["username"], original_meal.creator.username)

    def test_update_meal_recipes_ok(self):
        original_meal = MealFactory(creator=self.user1)
        breakfast_recipe = RecipeFactory()
        lunch_recipe_1 = RecipeFactory()
        lunch_recipe_2 = RecipeFactory()
        lunch_recipe_3 = RecipeFactory()
        dinner_recipe = RecipeFactory()

        body = {
            "breakfast": [breakfast_recipe.id],
            "lunch": [lunch_recipe_1.id, lunch_recipe_2.id, lunch_recipe_3.id],
            "dinner": [dinner_recipe.id],
        }
        response = self.make_update_meal_call(
            uuid=original_meal.id, data=body, user=self.user1
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["breakfast"][0]["id"], breakfast_recipe.id)
        self.assertEqual(len(response.content["breakfast"]), 1)
        self.assertEqual(len(response.content["lunch"]), 3)
        self.assertEqual(response.content["dinner"][0]["id"], dinner_recipe.id)
        self.assertEqual(len(response.content["dinner"]), 1)

    def test_update_meal_readonly_fields(self):
        original_meal = MealFactory(creator=self.user1)
        body = {
            "id": 123456,
            "creator": self.user2,
        }
        response = self.make_update_meal_call(
            uuid=original_meal.id, data=body, user=self.user1
        )

        content = response.content
        self.assertEqual(response.status_code, HTTP_200_OK)
        # check that fields are not updated
        self.assertEqual(content["id"], original_meal.id)
        self.assertEqual(content["creator"]["id"], original_meal.creator.id)
        self.assertEqual(content["creator"]["username"], original_meal.creator.username)

    def test_update_meal_no_token(self):
        meal = MealFactory(creator=self.user1)
        response = self.make_update_meal_call(
            uuid=meal.id,
            data={},
        )
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_update_meal_other_user(self):
        meal = MealFactory(creator=self.user1)
        response = self.make_update_meal_call(
            uuid=meal.id,
            user=self.user2,
            data={},
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_update_meal_wrong_id(self):
        response = self.make_update_meal_call(
            uuid=1234923874,
            user=self.user1,
            data={},
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_meal_no_token(self):
        meal = MealFactory()
        response = self.make_delete_meal_call(
            uuid=meal.id,
        )
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_delete_meal_other_creator(self):
        user2_meal = MealFactory(creator=self.user2)
        response = self.make_delete_meal_call(uuid=user2_meal.id, user=self.user1)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_meal_not_found(self):
        response = self.make_delete_meal_call(uuid=345345345, user=self.user1)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_meal_ok(self):
        meal_to_delete = MealFactory(creator=self.user1)
        response = self.make_delete_meal_call(uuid=meal_to_delete.id, user=self.user1)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

        response = self.make_retrieve_meal_call(uuid=meal_to_delete.id, user=self.user1)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
