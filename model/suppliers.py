from extension import db
from model.products import Product


class Supplier(db.Model):
    __tablename__ = 'suppliers'
    supplier_id = db.Column(db.SmallInteger, primary_key=True)
    company_name = db.Column(db.String(40), nullable=False)
    contact_name = db.Column(db.String(30))
    contact_title = db.Column(db.String(30))
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    phone = db.Column(db.String(24))
    fax = db.Column(db.String(24))
    homepage = db.Column(db.Text)
    suppliers = db.relationship(Product, backref='suppliers', lazy='select')

    @classmethod
    def find_by_id(cls, supplier_id):
        return Supplier.query.filter_by(supplier_id=supplier_id).first()

    def to_dict(self, supplier_id):
        customer = Supplier.find_by_id(supplier_id)
        data = {}
        for key, value in customer.__dict__.items():
            data[key] = value
        data.pop('_sa_instance_state')
        return data
