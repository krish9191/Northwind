

from model.employees import Employee
from flask_restful import Resource
from manager import get_customer_and_order_by_employee_id


class EmployeeInfo(Resource):
    """
    returns the information of employees by their respective id
    """

    def get(self, id):
        emp = Employee.find_by_id(id)
        return emp.to_json(emp.employee_id)


class CustomerAndOrderByEmployeeId(Resource):
    def get(self, id):
        return get_customer_and_order_by_employee_id(id)
