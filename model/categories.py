from extension import db
from manager import byte_array_to_json
from model.products import Product


class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.SmallInteger, primary_key=True)
    category_name = db.Column(db.String(15), nullable=False)
    description = db.Column(db.Text)
    picture = db.Column(db.LargeBinary)
    products = db.relationship(Product, backref='categories', lazy='select')

    @classmethod
    def find_by_id(cls, category_id):
        return Category.query.filter_by(category_id=category_id).first()

    def to_dict(self, category_id):
        category = Category.find_by_id(category_id)
        data = {}
        for key, value in category.__dict__.items():
            if type(value) == bytes:
                data[key] = byte_array_to_json(value)
            else:
                data[key] = value
        data.pop('_sa_instance_state')
        return data
