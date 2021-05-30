from flask import request
from manager import list_customer_order_by_employee


class ListCustomerOrderByEmployee:
    def get(self):
        data = request.get_json()
        return list_customer_order_by_employee(data['employee_id'])

