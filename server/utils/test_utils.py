from rest_framework.test import APIClient
from django.test.client import encode_multipart
import json
import datetime


class PATH:
    RECIPE = "/recipes/"
    CATEGORY = "/categories/"
    USER = "/users/"
    AUTH = "/auth/"
    FAVOURITE = "/favourites/"
    MEAL = "/meals/"


class API_ACTIONS:
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"
    GET = "get"


class CustomResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


def make_api_call(route, user, action=API_ACTIONS.GET, body={}, query_params={}):
    client = APIClient()
    if user:
        client.force_authenticate(user=user)

    content_type = "multipart/form-data;boundary=BoUnDaRyStRiNg"
    content = encode_multipart("BoUnDaRyStRiNg", body)
    if query_params:
        route = route.__add__("?")
        for key, value in query_params.items():
            route = f"{route}{key}={value}&"

    if action == API_ACTIONS.GET:
        response = client.get(route, content_type=content_type)
    elif action == API_ACTIONS.POST:
        response = client.post(route, content, content_type=content_type)
    elif action == API_ACTIONS.PUT:
        response = client.put(route, content, content_type=content_type)
    elif action == API_ACTIONS.PATCH:
        response = client.patch(route, content, content_type=content_type)
    elif action == API_ACTIONS.DELETE:
        response = client.delete(route, content, content_type=content_type)

    content = None
    if response.content:
        json_response = json.loads(response.content)
        content = json_response

    return CustomResponse(status_code=response.status_code, content=content)


def make_login_call(data):
    return make_api_call(
        route=PATH.AUTH + "login/", action=API_ACTIONS.POST, token=None, body=data
    )


def format_date(str_date):
    current_date_obj = datetime.datetime.strptime(str_date, "%Y-%m-%d")
    formatted_date = current_date_obj.strftime("%d/%m/%Y")
    return formatted_date
