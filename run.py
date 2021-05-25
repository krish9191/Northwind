from flask import Flask
from flask_restful import Api
from resources.list_employees_resource import EmployeeInfo
from resources.list_customers_resource import CustomerInfo
from resources.list_orders_resource import OrderInfo
from resources.list_products_resource import ProductInfo
from resources.list_categories_resource import CategoryInfo
from resources.list_suppliers_resource import SupplierInfo
from extension import db

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(EmployeeInfo, '/employees/<id>')
api.add_resource(CustomerInfo, '/customers/<id>')
api.add_resource(ProductInfo, '/products/<id>')
api.add_resource(OrderInfo, '/orders/<id>')
api.add_resource(CategoryInfo, '/categories/<id>')
api.add_resource(SupplierInfo, '/suppliers/<id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
