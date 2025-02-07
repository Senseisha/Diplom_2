class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    CREATE_URL = 'api/auth/register'
    LOGIN_URL = 'api/auth/login'
    DELETE_URL = 'api/auth/user'
    DATA_CHANGE = 'api/auth/user'
    ORDER_URL = 'api/orders'


class DataForResponse:
    existing_user = "User already exists"
    without_field = "Email, password and name are required fields"
    incorrect_login_password = "email or password are incorrect"
    without_auth = "You should be authorised"
    existing_email = "User with such email already exists"
    without_ingredient = "Ingredient ids must be provided"


class DataForCreate:
    CREATE_USER_BODY = {
        "email": "test-data@yandex.ru",
        "password": "password",
        "name": "Username"
    }


class DataForLogin:
    COURIER_LOGIN = {
        "email": "",
        "password": ""
    }


class DataForCreateOrder:
    CREATE_ORDER = {
        "ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]
    }

