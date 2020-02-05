from app import db

class ComicBook(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    autor = db.Column(db.String(255))
    publisher = db.Column(db.String(255))

    def __init__(self, name, autor, publisher):
        self.name = name
        self.autor = autor
        self.publisher = publisher

    def __repr__(self):
        return '<ComicBook %d>'%self.id