from extension import db


class CustomerDemographics(db.Model):
    __tablename__ = 'customer_demographics'
    customer_type_id = db.Column(db.LargeBinary, primary_key=True, nullable=False)
    customer_desc = db.Column(db.Text)
