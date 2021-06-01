from flask_restful import Resource
from model.suppliers import Supplier


class SupplierInfo(Resource):
    def get(self, id):
        supplier = Supplier.find_by_id(id)
        return supplier.to_dict(id)
