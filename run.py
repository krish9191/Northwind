from flask import Flask
from flask_restful import Api
from resources.list_employees_resource import EmployeeInfo
from resources.list_customers_resource import CustomerInfo
from resources.list_orders_resource import OrderInfo
from extension import db

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(EmployeeInfo, '/employees/<id>')
api.add_resource(CustomerInfo, '/customers/<id>')
api.add_resource(OrderInfo, '/orders/<id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
