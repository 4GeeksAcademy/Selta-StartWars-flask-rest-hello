"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Add new user
@app.route('/user', methods=['POST'])
def handle_new_user():
    req_body = request.get_json ()
    user_email = req_body ['email']
    user_password = req_body ['password']
    user_username = req_body ['username']
    user_is_active = req_body['is_active']

    new_user = User (email=user_email, password=user_password, is_active=user_is_active, username=user_username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify ({'Message': 'Created a new user'}), 200

# gets a list of all the users in the database
@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    serialized_users = [user.serialize() for user in users]
    
    if len(serialized_users) > 0:
        return jsonify(serialized_users), 200
    return jsonify ({'Message': 'No users in database'}), 404
    
# gets a list of all the people in the database
@app.route('/people', methods=['GET'])
def get_people():

# Adds a new person to people
@app.route('/person', methods=['POST'])
def add_person():

# gets a single person from the database through ID
@app.route('/person/<int:person_id>', methods=['GET'])
def get_person(person_id):

# gets all the favorites that belong to the user ID
@app.route('/users/favorite/<int:user_id>', methods=['GET'])
def get_all_favorites (user_id):
    
# adds a new planet
@app.route('/planets', methods=['POST'])
def add_planet():

# gets the list of all planets
@app.route('/planets', methods=['GET'])
def get_planets():

# gets a certain planet ID info
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet():

# add a new favorite planet to the current user 
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet (planet_id):

# add a new favorite person to the current user 
@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_person (person_id):

#deletes favorite planet with the id = planet_id
@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet (planet_id):

#deletes favorite people with the id = people_id
@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_person (person_id):

    



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
