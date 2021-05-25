from flask_restful import Resource
from model.products import Product


class ProductInfo(Resource):
    def get(self, id):
        product = Product.find_by_id(id)
        return product.to_dict(product.product_id)
