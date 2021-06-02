
from flask_restful import Resource
from manager import add_territory


class AddTerritory(Resource):
    def post(self, id):
        return add_territory(id)
