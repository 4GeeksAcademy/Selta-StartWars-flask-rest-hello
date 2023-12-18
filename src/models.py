from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorites (db.Model):
    __tablename__ = 'favorites'
    id = db.Column (db.Integer, primary_key=True)
    user_id = db.Column (db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column (db.Integer,db.ForeignKey('planet.id'),nullable=True)
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
    