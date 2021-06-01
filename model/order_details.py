from sqlalchemy import PrimaryKeyConstraint
from extension import db


class OrderDetail(db.Model):
    __tablename__ = 'order_details'
    order_id = db.Column(db.SmallInteger, db.ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.String, db.ForeignKey('products.product_id'), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.SmallInteger, nullable=False)
    discount = db.Column(db.Float, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('order_id', 'product_id'),
        {},
    )

    def __init__(self, product_id, unit_price, quantity, discount):
        self.product_id = product_id
        self.unit_price = unit_price
        self.quantity = quantity
        self.discount = discount
