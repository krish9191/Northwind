from extension import db
from model.categories import Category
from model.customers import Customer
from model.employees import Employee
from model.order_details import OrderDetail
from model.orders import Order
from model.products import Product
from model.regions import Region, Territory
from flask import jsonify, request
from model.suppliers import Supplier


def add_region(description):
    region_description = description
    region = Region(region_description)
    db.session.add(region)
    db.session.commit()
    return jsonify(
        region_description=description
    )


def add_territory(region_id):
    region = Region.find_by_id(region_id)
    if region is None:
        return {'error': 'region id not found'}, 404
    data = request.get_json()
    territory_description = data["description"]
    territory = Territory(territory_description)
    region.territories.append(territory)

    db.session.commit()
    return jsonify(
        territory_description=territory_description

    )


def get_order_details(order_id):
    order = Order.find_by_id(order_id)
    if order is None:
        return {'error': 'id not found'}, 404
    orders = db.session.query(OrderDetail.product_id, OrderDetail.unit_price, OrderDetail.quantity,
                              OrderDetail.discount).join(Order).filter(order_id == Order.order_id).all()

    result = []
    for order in orders:
        data = dict()
        data['product_id'] = order.product_id
        data['unit_price'] = order.unit_price
        data['quantity'] = order.quantity
        data['discount'] = order.discount
        result.append(data)
    return result


def count_orders_by_country():
    order = db.session.query(db.func.count(Order.ship_country), Order.ship_country).group_by(
        Order.ship_country).all()
    result = []
    for row in order:
        data = dict()
        data['count'] = row[0]
        data['country'] = row[1]
        result.append(data)
    return result


def get_customer_and_order_by_employee_id(employee_id):
    employee = Employee.find_by_id(employee_id)
    if employee is None:
        return {'error': 'id not found'}, 404

    query = db.session.query(Employee.last_name, Employee.first_name, Employee.region, Customer.contact_name,
                             Customer.company_name, Order.ship_city, Order.ship_city).join(Employee).join(
        Customer).filter(Employee.employee_id == employee_id).all()
    result_in_list = []
    for row in query:
        data = dict()
        data['lastname'] = row.last_name
        data['firstname'] = row.first_name
        data['region'] = row.region
        data['customer_name'] = row.contact_name
        data['company_name'] = row.company_name
        data['ship_city'] = row.ship_city
        data['ship_region'] = row.ship_city
        result_in_list.append(data)
    return result_in_list


def count_customer_per_countries():
    query = db.session.query(db.func.count(Customer.country), Customer.country).group_by(Customer.country).all()
    result = []
    for row in query:
        data = dict()
        data["number_of_customers"] = row[0]
        data["name_of_country"] = row[1]
        result.append(data)
    return result


def calculate_revenue_per_year(start_year, end_year):
    query = db.session.query(db.func.sum(OrderDetail.quantity * (OrderDetail.unit_price - OrderDetail.discount * 100))) \
        .join(Order).filter(Order.order_date.between(f'"{start_year}-01-01"', f'"{end_year}-01-01"')).one()

    return jsonify(
        total_revenue=format(query[0], '.2f')
    )


def calculate_revenue_per_supplier(supplier_id):
    supplier = Supplier.find_by_id(supplier_id)
    if supplier is None:
        return {'error': 'id not found'}, 404
    query = db.session.query(db.func.sum(Product.units_on_order * Product.unit_price)).join(Supplier).filter(
        Product.supplier_id == supplier_id).one()
    return {'total revenue': format(query[0], '.2f')}


def calculate_revenue_per_category(category_id):
    category = Category.find_by_id(category_id)
    if category is None:
        return {'error': 'id not found'}, 404
    query = db.session.query(db.func.sum(Product.units_on_order * Product.unit_price)).join(Category).filter(
        Product.category_id == category_id).one()
    return {'total revenue': format(query[0], '.2f')}
