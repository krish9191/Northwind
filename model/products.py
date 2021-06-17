from extension import db


class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.SmallInteger, primary_key=True)
    product_name = db.Column(db.String(40), nullable=False)
    supplier_id = db.Column(db.SmallInteger, db.ForeignKey('suppliers.supplier_id'), nullable=False)
    category_id = db.Column(db.SmallInteger, db.ForeignKey('categories.category_id'))
    quantity_per_unit = db.Column(db.String(20))
    unit_price = db.Column(db.Float(15))
    units_in_stock = db.Column(db.SmallInteger)
    units_on_order = db.Column(db.SmallInteger)
    reorder_level = db.Column(db.SmallInteger)
    discontinued = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_by_id(cls, product_id):
        return Product.query.filter(Product.product_id == product_id).first()

    def to_dict(self, product_id):
        product = Product.find_by_id(product_id)
        data = {}
        for key, value in product.__dict__.items():
            data[key] = value
        data.pop('_sa_instance_state')
        return data
