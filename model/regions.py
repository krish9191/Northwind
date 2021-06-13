from extension import db
from model.id_generator import IdGenerator
from model.territories import Territory


class Region(db.Model, IdGenerator):
    __tablename__ = 'region'
    region_id = db.Column(db.SmallInteger, primary_key=True)
    region_description = db.Column(db.String(40), nullable=False)
    territories = db.relationship(Territory, backref='regions', lazy='select')

    def __init__(self, description):
        IdGenerator.__init__(self, id="region_id")
        self.region_id = self.generate_id(Region.region_id)
        self.region_description = description

    @classmethod
    def find_by_id(cls, id):
        return Region.query.filter(Region.region_id == id).first()
