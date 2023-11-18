import sender_stand_request
import data

# Создаём заказ и проверяем, что код ответа равен 201
def test_order():
    order_response = sender_stand_request.post_create_order(data.body)
    assert order_response.status_code == 201

# Получаем заказ по треку и проверяем, что код равен 200
def test_order_receive():
    order_receive = sender_stand_request.get_receive_order()
    assert order_receive.status_code == 200





