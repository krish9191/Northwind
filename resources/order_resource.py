from flask import request

from model.orders import Order
from flask_restful import Resource
from manager import count_orders_by_country, count_orders_by_countries


class OrderInfo(Resource):
    def get(self, id):
        order = Order.find_by_id(id)
        return order.to_json(order.order_id)


class OrderByCountry(Resource):
    def get(self):
        return count_orders_by_countries()


class OrderBySpecificCountry(Resource):
    def get(self):
        data = request.get_json()
        return count_orders_by_country(data['country'])
