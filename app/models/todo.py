from .base import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.task
