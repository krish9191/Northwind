from flask_restful import Resource

from manager import get_order_details


class OrdersDetail(Resource):
    def get(self, id):
        return get_order_details(id)




