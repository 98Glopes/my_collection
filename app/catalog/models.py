from app import db

class ComicBook(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    autor = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    description = db.Column(db.String(700))

    def __init__(self, name, autor, publisher, description):
        self.name = name
        self.autor = autor
        self.publisher = publisher
        self.description = description

    def __repr__(self):
        return '<ComicBook %d>'%self.id 