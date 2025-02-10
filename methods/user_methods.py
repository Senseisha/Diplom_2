import requests
from data import Url


class UserMethods:
    def create_user(self, body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_URL}', data=body)

    def login_user(self, email, password):
        payload = {'email': email, 'password': password}
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data=payload)

    def change_data(self, payload, token):
        return requests.patch(f'{Url.BASE_URL}{Url.DATA_CHANGE}', data=payload, headers={
            "Authorization": token})

    def delete_user(self, access_token):
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_URL}', headers={
            "Authorization": access_token})
