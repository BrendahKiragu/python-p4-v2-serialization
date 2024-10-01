# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Welcome to the pet directory!'}
    return make_response(body, 200)

@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()

    if pet:
        resp_body = pet.to_dict()
        resp_status = 200
    else:
        resp_body = {'message': "Pet {id} not found."}    
        resp_status = 404
    return make_response(resp_body, resp_status)    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
