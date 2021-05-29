# from extension import db
#
#
# class OrderDetail(db.Model):
#     __tablename__ = 'order_details'
#     id = db.Column(db.SmallInteger, primary_key=True)
#     order_id = db.Column(db.SmallInteger, db.ForeignKey('order_id'), nullable=False)
#     product_id = db.Column(db.String, db.ForeignKey('product_id'))
#     unit_price = db.Column(db.Float, nullable=False)
#     quantity = db.Column(db.SmallInteger, nullable=False)
#     discount = db.Column(db.Float, nullable=False)
#     total = db.Column(db.Float)
#
#
#     @classmethod
#     def find_by_id(cls, id):
#         return OrderDetail.query.filter_by(id=id).first()
#
#     def to_dict(self, order_id):
#         order_detail = OrderDetail.find_by_id(order_id)
#         data = {}
#         for key, value in product.__dict__.items():
#             data[key] = value
#         data.pop('_sa_instance_state')
#         return data