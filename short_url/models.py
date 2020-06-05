from datetime import datetime
from short_url import db

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(150), nullable=False)
    short_url = db.Column(db.String(50), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_accessed = db.Column(db.DateTime, nullable=True)
    accessed = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Links(id: {self.id}, url: {self.url}, short_url: {self.short_url}, date_created: {self.date_created})"
