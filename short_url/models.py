from short_url import db

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False)
    short_url = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Links(id: {self.id}, url: {self.url}, short_url: {self.short_url})"
