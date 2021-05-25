from flask_restful import Resource
from model.categories import Category


class CategoryInfo(Resource):
    def get(self, id):
        category = Category.find_by_id(id)
        return category.to_dict(id)
