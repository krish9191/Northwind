from flask import request
from flask_restful import Resource

from manager import calculate_revenue_per_year, calculate_revenue_per_supplier


class RevenuePerYear(Resource):
    def get(self):
        data = request.get_json()
        return calculate_revenue_per_year(data['start_year'], data['end_year'])


class RevenuePerSupplier(Resource):
    def get(self, id):
        return calculate_revenue_per_supplier(id)