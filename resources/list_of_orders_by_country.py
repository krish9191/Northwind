from flask_restful import Resource
from manager import total_count_orders_by_country


class OrderByCountry(Resource):
    def get(self):
        return total_count_orders_by_country()
