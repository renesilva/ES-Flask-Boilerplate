from .base import db

class ToDo(db.Model):
    __tablename__ = 'ToDo'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    done = db.Column(db.Boolean, default=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return self.task
