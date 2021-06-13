from flask import request
from flask_restful import Resource

from manager import calculate_revenue_per_year, calculate_revenue_per_supplier, calculate_revenue_per_category


class RevenuePerYear(Resource):
    def get(self):
        args = request.args
        start_year = args['start']
        end_year = args['end']
        return calculate_revenue_per_year(start_year, end_year)


class RevenuePerSupplier(Resource):
    def get(self, id):
        return calculate_revenue_per_supplier(id)


class RevenuePerCategory(Resource):
    def get(self, id):
        return calculate_revenue_per_category(id)
