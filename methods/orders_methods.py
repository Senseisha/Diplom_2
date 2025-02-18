import requests
from data import Url


class OrdersMethods:
    def create_order(self, body, token):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', data=body, headers={
            "Authorization": token})

    def get_list_of_orders(self, token):
        return requests.get(f'{Url.BASE_URL}{Url.ORDER_URL}', headers={
            "Authorization": token})
