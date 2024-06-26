from flask import request
from flask_restx import Resource, fields

from models.client import clientModel
from schemas.client import clientSchema

from server.instance import server

client_ns = server.client_ns

client_schema = clientSchema()

ITEM_NOT_FOUND = 'Client not Found'
INVALID_CREDENTIALS = 'Invalid Credentials'

item = client_ns.model('Client', {
    'Name': fields.String(description='Client Name'),
    'Email': fields.String(description='Client Email'),
    'Password': fields.String(description='Client Password'),
})

login_model = client_ns.model('Login', {
    'Email': fields.String(description='Client Email', required=True),
    'Password': fields.String(description='Client Password', required=True),
})

class Client(Resource):
    def post(self):
        data = request.get_json()  
        client = ClientModel(**data) 
        try:
            client.save_to_db()  
            return {'message': 'Client created successfully'}, 201
        except:
            return {'message': 'An error occurred while creating the client'}, 500
    
    def get(self, id):
        client_data = clientModel.find_by_id(id)
        if client_data: 
            return client_schema.dump(client_data), 200
        return{'message': ITEM_NOT_FOUND }, 404

class ClientList(Resource):    
    
    def get(self, ):
        return client_list_schema.dump(clientModel.find_all()), 200
    
    @client_ns.expect(item)
    @client_ns.doc('Create an item')
    def post(self, ):
        client_json = request.get_json()
        client_data = client_schema.load(client_json)
        
        client_data.save_to_db()
        
        return client_schema.dump(client_data), 201

class Login(Resource):
    @client_ns.expect(login_model)
    def post(self):
        login_data = request.get_json()
        email = login_data.get('Email')
        password = login_data.get('Password')

        client = clientModel.find_by_email(email)
        if client and client.check_password(password): 
            return {'message': 'Login successful', 'client': client_schema.dump(client)}, 200
        else:
            return {'message': INVALID_CREDENTIALS}, 401