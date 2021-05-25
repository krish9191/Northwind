from extension import db


class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.String, primary_key=True, nullable=False)
    company_name = db.Column(db.String(40), nullable=False)
    contact_name = db.Column(db.String(30))
    contact_title = db.Column(db.String(30))
    address = db.Column(db.String(15))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    phone = db.Column(db.String(24))
    fax = db.Column(db.String(24))

    @classmethod
    def find_by_id(cls, customer_id):
        return Customer.query.filter_by(customer_id=customer_id).first()

    def to_dict(self, customer_id):
        customer = Customer.find_by_id(customer_id)
        data = {}
        for key, value in customer.__dict__.items():
            data[key] = value
        data.pop('_sa_instance_state')
        return data


class CustomerDemographics(db.Model):
    __tablename__ = 'customer_demographics'
    customer_type_id = db.Column(db.LargeBinary, Primary_key=True, nullable=False)
    customer_desc = db.Column(db.Text)


class CustomerCustomerDemo(db.Model):
    __tablename__ = 'customer_customer_demo'
    customer_id = db.Column(db.LargeBinary, db.ForeignKey('customer_id'), nullable=False)
    customer_type_id = db.Column(db.LargeBinary, db.ForeignKey('customer_type_id'), nullable=False)


