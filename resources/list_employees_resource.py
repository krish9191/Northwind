from flask_restful import Resource
from model.employees import Employee


class EmployeeInfo(Resource):
    def get(self, id):
        emp = Employee.find_by_id(id)
        return emp.to_json(emp.employee_id)
