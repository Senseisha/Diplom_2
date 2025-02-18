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
    internal_server_error_text = 'Internal Server Error'


class DataForCreateOrder:
    CREATE_ORDER = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }


class DataForCreateOrderWithInvalidHash:
    CREATE_ORDER = {
        "ingredients": ["abrakadabra789456123", "123456789abrakadabra"]
    }
