import requests
import configuration
import data



# Создание заказа
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)
response = post_create_order(data.body)

# Получение трека заказа
cod = response.json()


# Сохранение трека
def create_orders():
    Order_body = post_create_order(data.body)
    return Order_body

code = cod['track']
codes = str(code)

# Получение данных заказа по треку
def get_receive_order():
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDERS + codes)
response = get_receive_order()