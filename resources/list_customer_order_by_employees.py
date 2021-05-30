from flask_restful import Resource
from manager import list_customer_order_by_employee


class ListCustomerOrderByEmployee(Resource):
    def get(self, id):
        return list_customer_order_by_employee(id)

