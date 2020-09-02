from sql_alchemy_db_instance import db


class Assignments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500))
    input = db.Column(db.String(500))
    response = db.Column(db.String(500))
    done = db.Column(db.Boolean)
