import allure
from data import DataForResponse


class TestGetOrders:
    @allure.title('Test successful getting orders with authorization')
    def test_getting_orders_with_authorization(self, create_login_delete_user, order_methods):
        token = create_login_delete_user[1]
        get_orders = order_methods.get_list_of_orders(token)
        assert get_orders.status_code == 200 and get_orders.json()['success'] is True

    @allure.title('Test unsuccessful getting orders without authorization')
    def test_getting_orders_without_authorization(self, create_user_and_delete_user, order_methods):
        invalid_token = ''
        get_orders = order_methods.get_list_of_orders(invalid_token)
        assert get_orders.status_code == 401 and get_orders.json()['message'] == DataForResponse.without_auth
