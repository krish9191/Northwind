from extension import db


class USState(db.Model):
    __tablename__ = 'us_state'
    state_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    state_name = db.Column(db.String(100))
    state_abbr = db.Column(db.String)
    state_region = db.Column(db.String(40))

