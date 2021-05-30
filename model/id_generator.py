from extension import db


class IdGenerator:
    @classmethod
    def generate_id(cls, model_class, id_attribute):
        row = db.session.query(model_class.id_attribute).order_by(model_class.id_attribute.desc()).limit(1).one()
        result = row[0] + 1
        return result
