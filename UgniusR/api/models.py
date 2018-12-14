from UgniusR import db


class Course(db.Model):
    __tablename__ = 'Courses'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(128), index=True, unique=True)
    term = db.Column(db.String(500))

    def __init__(self, course, name, term):
        self.course = course
        self.name = name
        self.term = term

    def __repr__(self):
        return '<Course {}>'.format(self.course)
