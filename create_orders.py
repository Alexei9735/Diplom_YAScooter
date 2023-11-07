import configuration
import data
import requests

def post_new_order(body):     #Создание нового заказа
   return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER, json=body)

def save_track():     #Получение номера трека
   response = post_new_order(data.body_create_order)
   return response.json()["track"]

def get_receive_order_track():     #Получение заказа по номеру трека
   t = save_track()
   order = configuration.GET_ORDER_INFORMATION_BY_TRACK
   order = order+"?t=" + str(t)
   return requests.get(configuration.URL_SERVICE + order)