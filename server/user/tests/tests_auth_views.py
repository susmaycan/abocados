from django.contrib.auth.tokens import (PasswordResetTokenGenerator,
                                        default_token_generator)
from django.test import TestCase
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED)

from user.tests.factories import UserFactory
from utils.test_utils import API_ACTIONS, PATH, make_api_call


class AuthTestCase(TestCase):
    def setUp(self):
        self.logged_user = UserFactory(password="awesome-password-yay")

    def make_signup_call(self, data):
        return make_api_call(
            route=PATH.AUTH + "signup/", action=API_ACTIONS.POST, user=None, body=data
        )

    def make_login_call(self, data):
        return make_api_call(
            route=PATH.AUTH + "login/", action=API_ACTIONS.POST, user=None, body=data
        )

    def make_authenticated_call(self, user=None):
        return make_api_call(
            route=PATH.AUTH + "authenticated/",
            action=API_ACTIONS.GET,
            user=user,
        )

    def make_validate_email_call(self, data):
        return make_api_call(
            route=PATH.AUTH + "activate_account/",
            action=API_ACTIONS.POST,
            user=None,
            body=data,
        )

    def make_password_recovery_request(self, data):
        return make_api_call(
            route=PATH.AUTH + "password_recovery_request/",
            action=API_ACTIONS.POST,
            user=None,
            body=data,
        )

    def make_password_recovery_check(self, data):
        return make_api_call(
            route=PATH.AUTH + "password_recovery_check/",
            action=API_ACTIONS.POST,
            user=None,
            body=data,
        )

    def make_password_recovery_confirm(self, data):
        return make_api_call(
            route=PATH.AUTH + "password_recovery_confirm/",
            action=API_ACTIONS.POST,
            user=None,
            body=data,
        )

    def _get_signup_request(self, email=None, username=None, password=None):
        user = UserFactory()
        data = {
            "email": email or user.email,
            "password": password or "awesome-password-yay",
            "username": username or user.username,
        }
        return data

    def _get_login_request(self, email=None, password=None):
        data = {
            "email": email or self.logged_user.email,
            "password": password or "awesome-password-yay",
        }
        return data

    def test_signup_ok(self):
        user = UserFactory.build()
        body = self._get_signup_request(email=user.email, username=user.username)
        response = self.make_signup_call(body)

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.content["email"], user.email)
        self.assertEqual(response.content["username"], user.username)
        self.assertEqual(response.content["picture"], None)
        self.assertEqual(response.content["name"], None)
        self.assertNotIn("password", response.content)

    def test_signup_empty_fields(self):
        body = self._get_signup_request()
        body["email"] = ""
        body["password"] = ""
        body["username"] = ""

        response = self.make_signup_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "This field may not be blank.")
        self.assertEqual(
            response.content["password"][0], "This field may not be blank."
        )
        self.assertEqual(
            response.content["username"][0], "This field may not be blank."
        )

    def test_signup_without_mandatory_fields(self):
        body = {}
        response = self.make_signup_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "This field is required.")
        self.assertEqual(response.content["password"][0], "This field is required.")
        self.assertEqual(response.content["username"][0], "This field is required.")

    def test_signup_with_already_existing_email_username(self):
        body = self._get_signup_request(
            email=self.logged_user.email, username=self.logged_user.username
        )
        response = self.make_signup_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "This field must be unique.")
        self.assertEqual(response.content["username"][0], "This field must be unique.")

    def test_signup_wrong_email_format(self):
        body = self._get_signup_request(
            email="notanemail",
        )
        response = self.make_signup_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "Enter a valid email address.")

    def test_signup_wrong_password_min_length(self):
        body = self._get_signup_request(
            password="1234",
        )
        response = self.make_signup_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["password"][0],
            "Ensure this field has at least 8 characters.",
        )

    def test_signup_wrong_password_max_length(self):
        body = self._get_signup_request(
            password="x" * 500,
        )

        response = self.make_signup_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["password"][0],
            "Ensure this field has no more than 64 characters.",
        )

    def test_login_ok(self):
        body = self._get_login_request()
        response = self.make_login_call(body)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

        response_user = response.content["user"]
        self.assertEqual(response_user["email"], self.logged_user.email)
        self.assertEqual(response_user["username"], self.logged_user.username)
        self.assertEqual(response_user["name"], self.logged_user.name)
        self.assertIn("picture", response_user)
        self.assertNotIn("password", response_user)
        self.assertIn("access_token", response.content)

    def test_login_wrong_credentials(self):
        body = self._get_login_request(password="wrongpassword")

        response = self.make_login_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["non_field_errors"][0], "Invalid credentials")

    def test_login_empty_credentials(self):
        body = self._get_login_request()
        body["email"] = ""
        body["password"] = ""
        response = self.make_login_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "This field may not be blank.")
        self.assertEqual(
            response.content["password"][0], "This field may not be blank."
        )

    def test_login_without_mandatory_fields(self):
        body = {}
        response = self.make_login_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "This field is required.")
        self.assertEqual(response.content["password"][0], "This field is required.")

    def test_login_wrong_email_format(self):
        body = self._get_login_request(email="wrongpemailformat")
        response = self.make_login_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "Enter a valid email address.")

    def test_login_wrong_password_min_length(self):
        body = self._get_login_request(password="1234")
        response = self.make_login_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["password"][0],
            "Ensure this field has at least 8 characters.",
        )

    def test_login_wrong_password_max_length(self):
        body = self._get_login_request(password="x" * 500)
        response = self.make_login_call(body)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["password"][0],
            "Ensure this field has no more than 64 characters.",
        )

    def test_get_authenticated_user_ok(self):
        response = self.make_authenticated_call(user=self.logged_user)
        response_user = response.content
        self.assertEqual(response_user["email"], self.logged_user.email)
        self.assertEqual(response_user["username"], self.logged_user.username)
        self.assertEqual(response_user["name"], self.logged_user.name)
        self.assertIn("picture", response_user)
        self.assertNotIn("password", response_user)

    def test_get_authenticated_user_without_token(self):
        response = self.make_authenticated_call(user=None)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_validate_email_empty_token(self):
        body = {"user": "12345"}
        response = self.make_validate_email_call(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )

    def test_validate_email_empty_user_id(self):
        body = {"token": "12345"}
        response = self.make_validate_email_call(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )

    def test_validate_email_already_active(self):
        validated_user = UserFactory(is_active=True)
        encoded_user_id = urlsafe_base64_encode(force_bytes(validated_user.id))

        body = {"user": encoded_user_id, "token": "12345"}
        response = self.make_validate_email_call(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Email has already been verified"
        )

    def test_validate_email_ok(self):
        validated_user = UserFactory(is_active=False)
        encoded_user_id = urlsafe_base64_encode(force_bytes(validated_user.id))
        confirmation_token = default_token_generator.make_token(validated_user)

        body = {"user": encoded_user_id, "token": confirmation_token}
        response = self.make_validate_email_call(data=body)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_validate_email_wrxong_encoding(self):
        validated_user = UserFactory(is_active=True)

        body = {"user": validated_user.id, "token": "12345"}
        response = self.make_validate_email_call(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )

    def test_request_password_recovery_not_registered_email(self):
        body = {"email": UserFactory.build().email}
        response = self.make_password_recovery_request(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Email not registered"
        )

    def test_request_password_recovery_wrong_email_format(self):
        body = {"email": "wrongformatemail"}
        response = self.make_password_recovery_request(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "Enter a valid email address.")

    def test_request_password_recovery_none_email(self):
        response = self.make_password_recovery_request(data={})
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "This field is required.")

    def test_request_password_recovery_empty_email(self):
        response = self.make_password_recovery_request(data={"email": ""})
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["email"][0], "This field may not be blank.")

    def test_request_password_recovery_ok(self):
        user = UserFactory()

        body = {"email": user.email}
        response = self.make_password_recovery_request(data=body)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_check_password_recovery_empty_token(self):
        body = {"user": "12345"}
        response = self.make_password_recovery_check(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )

    def test_check_password_recovery_empty_user_id(self):
        body = {"token": "12345"}
        response = self.make_password_recovery_check(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )

    def test_check_password_recovery_user_doesnt_exit(self):
        encoded_user_id = urlsafe_base64_encode(force_bytes(88888888))

        body = {"user": encoded_user_id, "token": "12345"}
        response = self.make_password_recovery_check(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Email not registered"
        )

    def test_check_password_recovery_ok(self):
        user = UserFactory()

        encoded_user_id = urlsafe_base64_encode(force_bytes(user.id))
        reset_token = PasswordResetTokenGenerator().make_token(user)

        body = {"user": encoded_user_id, "token": reset_token}
        response = self.make_password_recovery_check(data=body)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_check_password_recovery_wrong_encoding(self):
        validated_user = UserFactory(is_active=True)

        body = {"user": validated_user.id, "token": "12345"}
        response = self.make_password_recovery_check(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )

    def test_confirm_password_recovery_empty_token(self):
        body = {"user": "12345", "password": "awesome-password-yay"}
        response = self.make_password_recovery_confirm(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )

    def test_confirm_password_recovery_empty_password(self):
        body = {
            "token": "12345",
            "user": "12345",
        }
        response = self.make_password_recovery_confirm(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content["password"][0], "This field is required.")

    def test_confirm_password_recovery_empty_data(self):
        body = {}
        response = self.make_password_recovery_confirm(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        # First checks password and then other fields
        self.assertEqual(response.content["password"][0], "This field is required.")

    def test_confirm_password_recovery_empty_user_id(self):
        body = {"token": "12345", "password": "awesome-password-yay"}
        response = self.make_password_recovery_confirm(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )

    def test_confirm_password_recovery_user_doesnt_exit(self):
        encoded_user_id = urlsafe_base64_encode(force_bytes(88888888))

        body = {
            "user": encoded_user_id,
            "token": "12345",
            "password": "awesome-password-yay",
        }
        response = self.make_password_recovery_confirm(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Email not registered"
        )

    def test_confirm_password_recovery_ok(self):
        user = UserFactory()
        encoded_user_id = urlsafe_base64_encode(force_bytes(user.id))
        reset_token = PasswordResetTokenGenerator().make_token(user)

        body = {
            "user": encoded_user_id,
            "token": reset_token,
            "password": "awesome-password-yay",
        }
        response = self.make_password_recovery_confirm(data=body)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_confirm_password_recovery_wrong_encoding(self):
        validated_user = UserFactory(is_active=True)

        body = {
            "user": validated_user.id,
            "token": "12345",
            "password": "awesome-password-yay",
        }
        response = self.make_password_recovery_confirm(data=body)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.content["non_field_errors"][0], "Token is invalid or expired"
        )
