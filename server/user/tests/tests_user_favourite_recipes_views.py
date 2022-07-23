from django.test import TestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from utils.test_utils import PATH, API_ACTIONS, make_api_call
from user.tests.factories import UserFactory
from recipe.tests.factories import RecipeFactory


class UsersFavouriteRecipesTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user2 = UserFactory()

    def make_retrieve_favourite_recipe_list(self, uuid, user=None):
        return make_api_call(
            route=PATH.USER + '%s' % (uuid) + PATH.FAVOURITE,
            action=API_ACTIONS.GET,
            user=user,
        )

    def make_add_favourite_recipe_call(self, uuid, data, user=None):
        return make_api_call(
            route=PATH.USER + '%s' % (uuid) + PATH.FAVOURITE + "add/",
            action=API_ACTIONS.POST,
            user=user,
            body=data
        )

    def make_delete_favourite_recipe_call(self, uuid, data, user=None):
        return make_api_call(
            route=PATH.USER + '%s' % (uuid) + PATH.FAVOURITE + 'delete/',
            action=API_ACTIONS.POST,
            user=user,
            body=data
        )

    def make_retrieve_recipe_call(self, uuid, user=None):
        return make_api_call(
            route=PATH.RECIPE + '%s/' % (uuid),
            user=user,
            action=API_ACTIONS.GET
        )

    def test_get_user_favourites_recipes_list__ok(self):
        recipes = RecipeFactory.create_batch(6, creator=self.user2)
        self.user.saved_recipes.set(recipes)

        response = self.make_retrieve_favourite_recipe_list(
            user=self.user,
            uuid=self.user.id
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content['count'], 6)

    def test_get_user_favourites_recipes_list__no_token(self):
        response = self.make_retrieve_favourite_recipe_list(
            uuid=self.user.id
        )
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_get_user_favourites_recipes_list__other_user(self):
        response = self.make_retrieve_favourite_recipe_list(
            uuid=self.user.id,
            user=self.user2
        )
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_add_favourite__ok(self):
        recipe = RecipeFactory(creator=self.user2)
        data = {
            'recipe': recipe.id
        }
        response = self.make_add_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user,
            data=data
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)

        response = self.make_retrieve_favourite_recipe_list(
            user=self.user,
            uuid=self.user.id
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content['count'], 1)

    def test_add_favourite__recipe_id_not_found(self):
        data = {
            'recipe': 123456
        }
        response = self.make_add_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user,
            data=data
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_add_favourite__recipe_id_already_favourited(self):
        recipe = RecipeFactory(creator=self.user2)
        self.user.saved_recipes.add(recipe)
        data = {
            'recipe': recipe.id
        }
        response = self.make_add_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user,
            data=data
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_add_favourite__other_user(self):
        response = self.make_add_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user2,
            data={}
        )
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_add_favourite__own_recipe(self):
        recipe = RecipeFactory(creator=self.user)
        data = {
            'recipe': recipe.id
        }
        response = self.make_add_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user,
            data=data
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_delete_favourite__ok(self):
        recipe = RecipeFactory(creator=self.user2)
        self.user.saved_recipes.add(recipe)
        data = {
            'recipe': recipe.id
        }
        response = self.make_delete_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user,
            data=data
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

        response = self.make_retrieve_favourite_recipe_list(
            user=self.user,
            uuid=self.user.id
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content['count'], 0)

    def test_delete_favourite__recipe_id_not_found(self):
        data = {
            'recipe': 123456
        }
        response = self.make_delete_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user,
            data=data
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_favourite__recipe_id_not_favourited(self):
        recipe = RecipeFactory(creator=self.user2)
        data = {
            'recipe': recipe.id
        }
        response = self.make_delete_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user,
            data=data
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_delete_favourite__other_user(self):
        response = self.make_delete_favourite_recipe_call(
            uuid=self.user.id,
            user=self.user2,
            data={}
        )
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_get_user_recipe_list__favourited_ok(self):
        recipe = RecipeFactory(creator=self.user2)
        self.user.saved_recipes.add(recipe)

        response = self.make_retrieve_recipe_call(
            uuid=recipe.id,
            user=self.user
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertTrue(response.content['favourited'])

        recipe2 = RecipeFactory(creator=self.user2)

        response = self.make_retrieve_recipe_call(
            uuid=recipe2.id,
            user=self.user
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertFalse(response.content['favourited'])
