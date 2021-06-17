from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from resources.employee_resource import EmployeeInfo, OrdersByEmployee
from resources.customer_resource import CustomerInfo, CustomerCountPerCountry
from resources.order_resource import OrderInfo, OrdersByCountry, OrdersCountByCountry
from resources.product_resource import ProductInfo
from resources.category_resource import CategoryInfo
from resources.supplier_resource import SupplierInfo
from resources.shipper_resource import ShipperInfo
from resources.region_resource import AddRegion
from resources.territory_resource import AddTerritory
from resources.order_detail_resource import OrdersDetail
from resources.revenue_resource import RevenuePerYear, RevenuePerSupplier, RevenuePerCategory
from extension import db
import os
from dotenv import load_dotenv

load_dotenv(".env")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
database = os.environ.get("DATABASE")

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'Northwind',
    'uiversion': 3,
    'specs_route': '/northwind'
}
swagger = Swagger(app, template_file='static/swagger.json', parse=True)

api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(EmployeeInfo, '/employees/<id>')
api.add_resource(CustomerInfo, '/customers/<id>')
api.add_resource(ProductInfo, '/products/<id>')
api.add_resource(OrderInfo, '/orders/<id>')
api.add_resource(CategoryInfo, '/categories/<id>')
api.add_resource(SupplierInfo, '/suppliers/<id>')
api.add_resource(ShipperInfo, '/shippers/<id>')
api.add_resource(AddRegion, '/regions')
api.add_resource(AddTerritory, '/territories')
api.add_resource(OrdersCountByCountry, '/orders_count/countries')
api.add_resource(OrdersByEmployee, '/employee/<id>/orders')
api.add_resource(CustomerCountPerCountry, '/customers_count/country')
api.add_resource(OrdersDetail, '/order_details/<id>')
api.add_resource(RevenuePerYear, '/revenue_per_year')
api.add_resource(RevenuePerSupplier, '/supplier/<id>/revenue')
api.add_resource(RevenuePerCategory, '/category/<id>/revenue')
api.add_resource(OrdersByCountry, '/orders/country')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
