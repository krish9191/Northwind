from extension import db
from datetime import date
from functions import byte_array_to_json, to_str_date


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.SmallInteger, primary_key=True)
    customer_id = db.Column(db.String, db.ForeignKey('customers.customer_id'))
    employee_id = db.Column(db.SmallInteger, db.ForeignKey('employees.employee_id'))
    order_date = db.Column(db.Date)
    required_date = db.Column(db.Date)
    shipped_date = db.Column(db.Date)
    ship_via = db.Column(db.SmallInteger, db.ForeignKey('shippers.shipper_id'))
    freight = db.Column(db.Float)
    ship_name = db.Column(db.String(40))
    ship_address = db.Column(db.String(60))
    ship_city = db.Column(db.String)
    ship_region = db.Column(db.String)
    ship_postal_code = db.Column(db.String(10))
    ship_country = db.Column(db.String(15))

    @classmethod
    def find_by_id(cls, order_id):
        return Order.query.filter_by(order_id=order_id).first()

    def to_json(self, order_id):
        order = Order.find_by_id(order_id)
        data = {}
        for key, value in order.__dict__.items():
            if type(value) == date:
                data[key] = to_str_date(value)
            elif type(value) == bytes:
                data[key] = byte_array_to_json(value)
            else:
                data[key] = value
        data.pop('_sa_instance_state')
        return data
