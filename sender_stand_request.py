import configuration
import requests

# Создание нового заказа
def post_create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


# Получение данных заказа по трек-номеру
def get_order_data(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))




