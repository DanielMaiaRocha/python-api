from flask import request
from flask_restx import Resource, fields

from models.cars import carsModel
from schemas.cars import CarsSchema

from server.instance import server

cars_ns = server.cars_ns

cars_schema = CarsSchema()
cars_list_schema = CarsSchema(many = True)

ITEM_NOT_FOUND = 'Cars not Found'

item = cars_ns.model('Cars', {
    'title': fields.String(description='Car name'),
    'pages': fields.Integer(default=0)
})

class Cars(Resource):
    
    def get(self, id):
        cars_data = carsModel.find_by_id(id)
        if cars_data: 
            return cars_schema.dump(cars_data), 200
        return {'message': ITEM_NOT_FOUND}, 404
    
class CarsList(Resource):
    
    def get(self, ):   
        return cars_list_schema.dump(carsModel.find_all()), 200
    
    
    @cars_ns.expect(item)
    @cars_ns.doc('Create an Item')
    def post(self, ):
        cars_json = request.get_json()
        cars_data = cars_schema.load(cars_json)
        
        cars_data.save_to_db()
        
        return cars_schema.dump(cars_data), 201