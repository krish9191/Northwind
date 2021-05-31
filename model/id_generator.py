from extension import db


class IdGenerator:
    def __init__(self, id):
        self.id = id

    def generate_id(self):
        row = db.session.query(str(self.__class__.__name__)).order_by(F"{self.id} desc").limit(1).one()
        result = row[0] + 1
        return result
