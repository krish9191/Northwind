from flask import Flask
from flask_restful import Api
from resources.employee_resource import EmployeeInfo, CustomerAndOrderByEmployeeId
from resources.customer_resource import CustomerInfo, CustomerPerCountry
from resources.order_resource import OrderInfo,  OrderByCountry
from resources.product_resource import ProductInfo
from resources.category_resource import CategoryInfo
from resources.supplier_resource import SupplierInfo
from resources.shipper_resource import ShipperInfo
from resources.region_resource import AddRegion
from resources.territory_resource import AddTerritory
from resources.order_detail_resource import OrdersDetail
from resources.revenue_resource import RevenuePerYear
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
api.add_resource(ShipperInfo, '/shippers/<id>')
api.add_resource(AddRegion, '/regions')
api.add_resource(AddTerritory, '/territories/<id>')
api.add_resource(OrderByCountry, '/order_by_country')
api.add_resource(CustomerAndOrderByEmployeeId, '/customer_and_order_by_employee_id/<id>')
api.add_resource(CustomerPerCountry, '/customer_per_country')
api.add_resource(OrdersDetail, '/order_details/<id>')
api.add_resource(RevenuePerYear, '/revenue_per_year')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
