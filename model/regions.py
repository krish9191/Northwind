from extension import db


class Region(db.Model):
    region_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    region_description = db.Column(db.String(40), nullable=False)
