from flask_restful import Resource
from model.orders import Order
from extension import db


class OrderByCountry(Resource):
    def get(self):
        order = db.session.query(db.func.count(Order.ship_country), Order.ship_country).group_by(
            Order.ship_country).all()
        result = []
        for row in order:
            data = dict()
            data['count'] = row[0]
            data['country'] = row[1]
            result.append(data)
        return result
