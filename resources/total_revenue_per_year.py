from flask_restful import Resource

from manager import calculate_revenue_per_year


class RevenuePerYear(Resource):
    def get(self):
        return calculate_revenue_per_year()

