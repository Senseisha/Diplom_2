import pytest

from generator import register_new_user
from methods.user_methods import UserMethods
from methods.orders_methods import OrdersMethods


@pytest.fixture()
def user_methods():
    return UserMethods()


@pytest.fixture()
def order_methods():
    return OrdersMethods()


@pytest.fixture()
def generate_users_data():
    create_users_body = register_new_user()
    return create_users_body


@pytest.fixture()
def generate_users_data_with_delete(generate_users_data):
    yield generate_users_data

    email = generate_users_data['email']
    password = generate_users_data['password']

    user_token = UserMethods().login_user(email, password).json().get('accessToken')
    if user_token:
        UserMethods().delete_user(user_token)


@pytest.fixture()
def create_user(generate_users_data):
    UserMethods().create_user(generate_users_data)
    return generate_users_data


@pytest.fixture()
def create_login_delete_user(generate_users_data):
    user_email = generate_users_data['email']
    user_password = generate_users_data['password']
    UserMethods().create_user(generate_users_data)

    user_response = UserMethods().login_user(user_email, user_password)
    user_response_json = user_response.json()
    user_token = user_response_json.get('accessToken')
    user_data = user_response_json.get('user')
    yield [user_response, user_token, user_data]

    UserMethods().delete_user(user_token)


@pytest.fixture()
def create_user_and_delete_user(generate_users_data):
    user_token = UserMethods().create_user(generate_users_data).json().get('accessToken')
    yield user_token

    UserMethods().delete_user(user_token)