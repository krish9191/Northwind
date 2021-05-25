from flask_restful import Resource
from model.orders import Order


class OrderInfo(Resource):
    def get(self, id):
        order = Order.find_by_id(id)
        return order.to_json(order.order_id)

