from flask import  jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.client import Client, ClientList, Login 
from flask_cors import CORS

from server.instance import server

api = server.api
app = server.app
CORS(app)

@app.route('/client', methods=['OPTIONS', 'GET', 'POST'])
def handle_options():
    response = jsonify({'message': 'Allowing CORS'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    return response

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Client, '/client/<int:id>')
api.add_resource(ClientList, '/client')
api.add_resource(Login, '/client/login')


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()   