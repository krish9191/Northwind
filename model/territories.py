from extension import db


class Territories(db.Model):
    __tablename__ = 'territories'
    territory_id = db.Column(db.String, primary_key=True, nullable=False)
    territory_description = db.Column(db.String(40), nullable=False)
    region_id = db.Column(db.SmallInteger, db.ForeignKey('region_id'), nullable=False)





