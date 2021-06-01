from flask_restful import Resource
from model.shippers import Shipper


class ShipperInfo(Resource):
    def get(self, id):
        shipper = Shipper.find_by_id(id)
        return shipper.to_dict(id)
