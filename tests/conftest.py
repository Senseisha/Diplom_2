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
    email = generate_users_data['email']
    password = generate_users_data['password']
    UserMethods().create_user(generate_users_data)

    user_login = UserMethods().login_user(email, password)
    user_token = user_login.json().get('accessToken')
    yield [user_login, user_token]

    UserMethods().delete_user(user_token)