from flask import request
from flask_restful import Resource
from manager import add_territory


class AddTerritory(Resource):
    def post(self):
        data = request.get_json()
        return add_territory(data['region_id'], data['territory_description'])
