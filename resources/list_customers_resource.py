from flask_restful import Resource
from model.customers import Customer


class CustomerInfo(Resource):
    def get(self, id):
        customer = Customer.find_by_id(id)
        return customer.to_dict(id)
