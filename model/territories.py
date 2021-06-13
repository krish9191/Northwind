import uuid

from extension import db


class Territory(db.Model):
    __tablename__ = 'territories'
    territory_id = db.Column(db.String, primary_key=True)
    territory_description = db.Column(db.String(40), nullable=False)
    region_id = db.Column(db.SmallInteger, db.ForeignKey('region.region_id'), nullable=False)

    def __init__(self, region_id, description):
        self.territory_id = str(uuid.uuid4())
        self.region_id = region_id
        self.territory_description = description

    @classmethod
    def find_by_id(cls, id):
        return Territory.query.filter(Territory.region_id == id).first()

