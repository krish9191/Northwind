from flask_restful import Resource

from manager import count_customer_per_countries


class CustomerPerCountry(Resource):
    def get(self):
        return count_customer_per_countries()
