from extension import db
from model.orders import Order


class Shipper(db.Model):
    __tablename__ = 'shippers'
    shipper_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    company_name = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(24))
    orders = db.relationship(Order, backref='shippers', lazy='select')

    @classmethod
    def find_by_id(cls, shipper_id):
        return Shipper.query.filter_by(shipper_id=shipper_id).first()

    def to_dict(self, shipper_id):
        shipper = Shipper.find_by_id(shipper_id)
        data = {}
        for key, value in shipper.__dict__.items():
            data[key] = value
        data.pop('_sa_instance_state')
        return data
