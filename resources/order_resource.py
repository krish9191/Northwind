from flask import request

from model.orders import Order
from flask_restful import Resource
from manager import count_orders_by_countries, get_orders_by_country


class OrderInfo(Resource):
    def get(self, id):
        order = Order.find_by_id(id)
        return order.to_json(order.order_id)


class OrdersCountByCountry(Resource):
    def get(self):
        return count_orders_by_countries()


class OrdersByCountry(Resource):
    def get(self):
        name = request.args.get('name')
        return get_orders_by_country(name)
