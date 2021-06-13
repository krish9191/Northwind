from model.customers import Customer
from flask_restful import Resource
from manager import count_customer_per_countries


class CustomerInfo(Resource):
    def get(self, id):
        customer = Customer.find_by_id(id)
        return customer.to_dict(id)


class CustomerCountPerCountry(Resource):
    def get(self):
        return count_customer_per_countries()
