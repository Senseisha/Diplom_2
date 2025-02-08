import allure
import pytest
from data import DataForResponse


class TestChangeUserData:
    @allure.title('Test successful change of user data with authorization')
    @pytest.mark.parametrize('key, data',
                             [['email', 'ilovecats@yandex.ru'], ['password', 'minikitty'], ['name', 'onlycats']])
    def test_change_user_data_with_authorization(self, key, data, create_login_delete_user, user_methods):
        token = create_login_delete_user[1]
        change_user_data = user_methods.change_data({key: data}, token)
        if key == 'password':
            assert change_user_data.status_code == 200
            return

        assert change_user_data.status_code == 200 \
               and change_user_data.json()['user'][key] == data

    @allure.title('Test unsuccessful change of user data without authorization')
    @pytest.mark.parametrize('key, data',
                             [['email', 'ilovecats@yandex.ru'], ['password', 'minikitty'], ['name', 'onlycats']])
    def test_change_user_data_without_authorization(self, key, data, create_user_and_delete_user, user_methods):
        invalid_token = ''
        change_user_data = user_methods.change_data({key: data}, invalid_token)
        assert change_user_data.status_code == 401 \
               and change_user_data.json()['message'] == DataForResponse.without_auth


