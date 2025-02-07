import requests
from data import Url


class OrdersMethods:
    def create_order(self, body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=body)

    def get_list_of_orders(self):
        return requests.get(f'{Url.BASE_URL}{Url.ORDER_URL}')
