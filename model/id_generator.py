from sqlalchemy import text

from extension import db


class IdGenerator:
    def __init__(self, id):
        self.id = id

    def generate_id(self, class_id):
        row = db.session.query(class_id).order_by(text(f'{self.id} desc')).limit(1).one()
        result = row[0] + 1
        return result
