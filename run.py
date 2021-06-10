from flasgger import Swagger
from flask import Flask
from flask_restful import Api


from resources.employee_resource import EmployeeInfo, CustomerAndOrderByEmployeeId
from resources.customer_resource import CustomerInfo, CustomerPerCountry
from resources.order_resource import OrderInfo, OrderByCountry, OrderBySpecificCountry
from resources.product_resource import ProductInfo
from resources.category_resource import CategoryInfo
from resources.supplier_resource import SupplierInfo
from resources.shipper_resource import ShipperInfo
from resources.region_resource import AddRegion
from resources.territory_resource import AddTerritory
from resources.order_detail_resource import OrdersDetail
from resources.revenue_resource import RevenuePerYear, RevenuePerSupplier, RevenuePerCategory
from extension import db


app = Flask(__name__)


app.config['SWAGGER'] = {
    'title': 'Northwind',
    'uiversion': 3,
    'specs_route': '/northwind'
}
swagger = Swagger(app, template_file='static/swagger.json', parse=True)

api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(EmployeeInfo, '/employees /<id>')
api.add_resource(CustomerInfo, '/customers/<id>')
api.add_resource(ProductInfo, '/products/<id>')
api.add_resource(OrderInfo, '/orders/<id>')
api.add_resource(CategoryInfo, '/categories/<id>')
api.add_resource(SupplierInfo, '/suppliers/<id>')
api.add_resource(ShipperInfo, '/shippers/<id>')
api.add_resource(AddRegion, '/regions')
api.add_resource(AddTerritory, '/territories/<id>')
api.add_resource(OrderByCountry, '/orders_by_countries')
api.add_resource(CustomerAndOrderByEmployeeId, '/orders_by_employee/<id>')
api.add_resource(CustomerPerCountry, '/customers_per_country')
api.add_resource(OrdersDetail, '/order_details/<id>')
api.add_resource(RevenuePerYear, '/revenue_per_year')
api.add_resource(RevenuePerSupplier, '/revenue_per_supplier/<id>')
api.add_resource(RevenuePerCategory, '/revenue_per_category/<id>')
api.add_resource(OrderBySpecificCountry, '/orders_by_country')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
