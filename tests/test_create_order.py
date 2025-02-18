import allure
from data import DataForResponse
from data import DataForCreateOrder
from data import DataForCreateOrderWithInvalidHash


class TestCreateOrder:
    @allure.title('Test successful order creation with authorization')
    def test_create_order_with_authorization(self, create_login_delete_user, order_methods):
        token = create_login_delete_user[1]
        create_order = order_methods.create_order(DataForCreateOrder.CREATE_ORDER, token)
        assert create_order.status_code == 200 and create_order.json()['success'] is True

    @allure.title('Test unsuccessful order creation without authorization')
    def test_create_order_without_authorization(self, create_user_and_delete_user, order_methods):
        invalid_token = ''
        create_order = order_methods.create_order(DataForCreateOrder.CREATE_ORDER, invalid_token)
        assert create_order.status_code == 401 and create_order.json()['message'] == DataForResponse.without_auth

    @allure.title('Test unsuccessful order creation without ingredients')
    def test_create_order_without_ingredients(self, create_login_delete_user, order_methods):
        token = create_login_delete_user[1]
        ingredients = ''
        create_order = order_methods.create_order(ingredients, token)
        assert create_order.status_code == 400 and create_order.json()['message'] == DataForResponse.without_ingredient

    @allure.title('Test unsuccessful order creation with invalid hash')
    def test_test_create_order_with_invalid_hash(self, create_login_delete_user, order_methods):
        token = create_login_delete_user[1]
        create_order = order_methods.create_order(DataForCreateOrderWithInvalidHash.CREATE_ORDER, token)
        assert create_order.status_code == 500 and DataForResponse.internal_server_error_text in create_order.text
