import allure
from data import DataForResponse


class TestLoginUser:
    @allure.title('Test successful user login')
    def test_successful_user_login(self, create_login_delete_user, user_methods):
        login_token = create_login_delete_user[1]
        response = create_login_delete_user[0]
        assert response.status_code == 200 and login_token

    @allure.title('Test unsuccessful user login with wrong password')
    def test_courier_login_with_wrong_login(self, create_user, user_methods):
        wrong_password = "abrakadabrakakayato"
        user_login = user_methods \
            .login_user(create_user["email"], wrong_password)
        assert user_login.status_code == 401 \
               and user_login.json()['message'] == DataForResponse.incorrect_login_password
