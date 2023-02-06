from django.test import TestCase
from rest_framework.status import (HTTP_200_OK, HTTP_204_NO_CONTENT,
                                   HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN,
                                   HTTP_404_NOT_FOUND)

from user.tests.factories import UserFactory
from utils.test_utils import API_ACTIONS, PATH, make_api_call


class UsersTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user2 = UserFactory()

    def make_retrieve_user_call(self, uuid, user=None):
        return make_api_call(
            route=PATH.USER + "%s/" % (uuid),
            action=API_ACTIONS.GET,
            user=user,
        )

    def make_update_user_call(self, uuid, data, user=None):
        return make_api_call(
            route=PATH.USER + "%s/" % (uuid),
            action=API_ACTIONS.PUT,
            user=user,
            body=data,
        )

    def make_delete_user_call(self, uuid, user=None):
        return make_api_call(
            route=PATH.USER + "%s/" % (uuid),
            action=API_ACTIONS.DELETE,
            user=user,
        )

    def make_retrieve_recipes_of_user(self, uuid, user=None):
        return make_api_call(
            route=PATH.USER + "%s" % (uuid) + PATH.RECIPE,
            action=API_ACTIONS.GET,
            user=user,
        )

    def test_get_user_by_id_ok(self):
        response = self.make_retrieve_user_call(user=self.user, uuid=self.user.id)

        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content["username"], self.user.username)
        self.assertIsNotNone(content["picture"])
        self.assertEqual(content["name"], self.user.name)
        self.assertNotIn("password", content)
        self.assertNotIn("email", content)

    def test_get_user_by_id_without_token(self):
        response = self.make_retrieve_user_call(user=None, uuid=self.user.id)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_get_user_by_id_not_found(self):
        response = self.make_retrieve_user_call(user=self.user, uuid=12345)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_update_user_name_ok(self):
        updated_name = "updated name"
        body = {
            "name": updated_name,
        }
        response = self.make_update_user_call(
            user=self.user, uuid=self.user.id, data=body
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["name"], updated_name)

    def test_cant_update_user_username_ok(self):
        new_username = "new_username"
        body = {
            "username": new_username,
        }
        response = self.make_update_user_call(
            user=self.user, uuid=self.user.id, data=body
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["username"], self.user.username)

    def test_update_user_email_ok(self):
        new_email = "brand_new_email@test.com"
        body = {
            "email": new_email,
        }
        response = self.make_update_user_call(
            user=self.user, uuid=self.user.id, data=body
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["email"], new_email)

        updated_user = self.user
        updated_user.email = new_email
        response = self.make_retrieve_user_call(user=updated_user, uuid=self.user.id)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_update_user_without_token(self):
        response = self.make_update_user_call(user=None, uuid=self.user.id, data={})
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_update_user_not_found(self):
        body = {
            "name": "another name",
        }
        response = self.make_update_user_call(user=self.user, uuid=123456, data=body)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_update_other_user(self):
        body = {
            "name": "another name",
        }
        response = self.make_update_user_call(
            user=self.user, uuid=self.user2.id, data=body
        )
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_delete_user_without_token(self):
        response = self.make_delete_user_call(
            user=None,
            uuid=self.user.id,
        )
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_delete_other_user(self):
        response = self.make_delete_user_call(
            user=self.user,
            uuid=self.user2.id,
        )
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_delete_user_not_found(self):
        response = self.make_delete_user_call(
            user=self.user,
            uuid=12345,
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_user_ok(self):
        response = self.make_delete_user_call(
            user=self.user,
            uuid=self.user.id,
        )
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

        response = self.make_retrieve_user_call(
            uuid=self.user.id,
            user=self.user,
        )
        # you can't acces it anymore
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
