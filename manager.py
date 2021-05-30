from extension import db
from model.customers import Customer
from model.employees import Employee
from model.orders import Order
from model.regions import Region, Territory
from flask import jsonify, request


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


def total_count_orders_by_country():
    order = db.session.query(db.func.count(Order.ship_country), Order.ship_country).group_by(
        Order.ship_country).all()
    result = []
    for row in order:
        data = dict()
        data['count'] = row[0]
        data['country'] = row[1]
        result.append(data)
    return result


def list_customer_order_by_employee(employee_id):
    employee = Employee.find_by_id(employee_id)
    if employee is None:
        return {'error': 'id not found'}, 404

    query = db.session.query(Employee.last_name, Employee.first_name, Employee.region, Customer.contact_name,
                             Customer.company_name, Order.ship_city, Order.ship_city)
    query = query.join(Employee).join(Customer)
    results = query.filter(Employee.employee_id == employee_id).all()
    result_in_list = []
    for row in results:
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
