from UgniusR import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(128), index=True, unique=True)
    term = db.Column(db.String(500))
