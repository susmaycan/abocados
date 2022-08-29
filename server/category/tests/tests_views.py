from django.test import TestCase
from rest_framework.status import (HTTP_200_OK, HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND)

from category.tests.factories import CategoryFactory
from user.tests.factories import UserFactory
from utils.test_utils import API_ACTIONS, PATH, make_api_call


class CategoryTestCase(TestCase):
    def setUp(self):
        self.user_admin = UserFactory(is_staff=True)
        self.user_member = UserFactory(is_staff=False)

    def make_retrieve_category_list_call(self, user=None, query_params={}):
        url = PATH.CATEGORY
        return make_api_call(
            route=url, user=user, action=API_ACTIONS.GET, query_params=query_params
        )

    def make_retrieve_category_call(self, uuid, user=None):
        return make_api_call(
            route=PATH.CATEGORY + "%s/" % (uuid), user=user, action=API_ACTIONS.GET
        )

    def make_create_category_call(self, data, user=None):
        return make_api_call(
            route=PATH.CATEGORY, user=user, action=API_ACTIONS.POST, body=data
        )

    def test_create_category_as_a_member(self):
        response = self.make_create_category_call(data={}, user=self.user_member)

        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_retrieve_category_list_ok(self):
        CategoryFactory.create_batch(5)
        # admin can see categories
        response = self.make_retrieve_category_list_call(user=self.user_admin)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 5)

        # members can also see categories
        response = self.make_retrieve_category_list_call(user=self.user_member)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 5)

    def test_retrieve_category_list_no_token(self):
        response = self.make_retrieve_category_list_call(user=None)

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_retrieve_category_by_id_as_admin_ok(self):
        category = CategoryFactory()
        response = self.make_retrieve_category_call(
            uuid=category.id, user=self.user_admin
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["name"], category.name)
        self.assertEqual(response.content["description"], category.description)
        self.assertEqual(response.content["type"], category.type)

    def test_retrieve_category_by_id_as_member_ok(self):
        category = CategoryFactory()
        response = self.make_retrieve_category_call(
            uuid=category.id, user=self.user_member
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["name"], category.name)
        self.assertEqual(response.content["description"], category.description)
        self.assertEqual(response.content["type"], category.type)

    def test_retrieve_category_by_id_no_token(self):
        category = CategoryFactory()
        response = self.make_retrieve_category_call(uuid=category.id, user=None)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_retrieve_category_by_id_not_found(self):
        response = self.make_retrieve_category_call(uuid=4567, user=self.user_admin)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
