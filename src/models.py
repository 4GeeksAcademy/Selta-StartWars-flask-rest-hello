from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String (20),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorite', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class Favorite (db.Model):
    __tablename__ = 'favorite'
    id = db.Column (db.Integer, primary_key=True)
    user_id = db.Column (db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column (db.Integer,db.ForeignKey('planets.id'),nullable=True)
    people_id = db.Column (db.Integer,db.ForeignKey('people.id'),nullable=True)


class People (db.Model):
    __tablename__ = 'people'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(100)) # does it need unique?
    age = db.Column (db.Integer)
    height = db.Column (db.Integer)
    

    def serialize (self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "height": self.height
        }
    
class Planets (db.Model):
    __tablename__ = 'planets'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(100)) # does it need unique?
    mass = db.Column (db.Integer)
    environment = db.Column (db.String (100))

    def serialize (self):
        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "environment": self.environment
        }
    