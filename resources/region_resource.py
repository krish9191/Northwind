from flask_restful import Resource
from flask import request
from manager import add_region


class AddRegion(Resource):
    def post(self):
        data = request.get_json()
        return add_region(data["region_description"])
