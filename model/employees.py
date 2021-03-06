from extension import db
from functions import to_str_date, byte_array_to_json
from datetime import date
from model.orders import Order
from model.regions import Territory

employee_territory = db.Table(
    'employee_territories',
    db.Column('employee_id', db.SmallInteger, db.ForeignKey('employees.employee_id'), nullable=False),
    db.Column('territory_id', db.String, db.ForeignKey('territories.territory_id'), nullable=False))


class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.SmallInteger, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    title = db.Column(db.String)
    title_of_courtesy = db.Column(db.String)
    birth_date = db.Column(db.Date)
    hire_date = db.Column(db.Date)
    address = db.Column(db.String)
    city = db.Column(db.String)
    region = db.Column(db.String)
    postal_code = db.Column(db.String)
    country = db.Column(db.String)
    home_phone = db.Column(db.String)
    extension = db.Column(db.String)
    photo = db.Column(db.LargeBinary)
    notes = db.Column(db.Text)
    reports_to = db.Column(db.SmallInteger)
    photo_path = db.Column(db.String)
    employee_territory = db.relationship(
        Territory, secondary=employee_territory, backref='employees', lazy='select')
    orders = db.relationship(Order, backref='employees', lazy='select')

    @classmethod
    def find_by_id(cls, employee_id):
        return Employee.query.filter(Employee.employee_id == employee_id).first()

    def to_json(self, emp_id):
        emp = Employee.find_by_id(emp_id)
        data = {}
        for key, value in emp.__dict__.items():
            if type(value) == date:
                data[key] = to_str_date(value)
            elif type(value) == bytes:
                data[key] = byte_array_to_json(value)
            else:
                data[key] = value
        data.pop('_sa_instance_state')
        return data
