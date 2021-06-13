

from model.employees import Employee
from flask_restful import Resource
from manager import get_orders_by_employee


class EmployeeInfo(Resource):
    """
    returns the information related to employee by their respective id
    """

    def get(self, id):
        emp = Employee.find_by_id(id)
        return emp.to_json(emp.employee_id)


class OrdersByEmployee(Resource):
    def get(self, id):
        return get_orders_by_employee(id)
