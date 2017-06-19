from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Datos(db.Model):
    __tablename__ = 'datos'
    name = db.Column(db.String(120), primary_key=True,unique=True)
    favorite_color = db.Column(db.String(120), unique=False)
    cats_dog = db.Column(db.Integer, unique=False)

    def __init__(self, name, favorite_color, cats_dog):
        self.name = name
        self.favorite_color = favorite_color
        self.cats_dog = cats_dog
