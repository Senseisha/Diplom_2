import allure
from data import DataForResponse


class TestCreateUser:
    @allure.title('Test successful user creation')
    def test_success_created_user(self, generate_users_data_with_delete, user_methods):
        user_response = user_methods.create_user(generate_users_data_with_delete)
        assert user_response.status_code == 200 and user_response.json()['success'] is True

    @allure.title('Test unsuccessful creating two identical users')
    def test_creating_two_identical_users(self, generate_users_data_with_delete, user_methods):
        user_methods.create_user(generate_users_data_with_delete)
        same_user_response = user_methods.create_user(generate_users_data_with_delete)
        assert same_user_response.status_code == 403 \
                and same_user_response.json()['message'] == DataForResponse.existing_user

    @allure.title('Test unsuccessful creating user without one field')
    def test_creating_user_without_one_field(self, generate_users_data_with_delete, user_methods):
        copy_data = generate_users_data_with_delete.copy()
        copy_data['password'] = ''
        user_response = user_methods.create_user(copy_data)
        assert user_response.status_code == 403 \
               and user_response.json()['message'] == DataForResponse.without_field
