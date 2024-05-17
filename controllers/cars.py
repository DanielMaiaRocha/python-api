from flask import request
from flask_restx import Resource, fields

from models.cars import carsModel
from schemas.cars import CarsSchema

from server.instance import server

cars_ns = server.cars_ns

cars_schema = CarsSchema()
cars_list_schema = CarsSchema(many = True)


class Cars(Resource):
    
    def get(self, id):
        cars_data = carsModel.find_by_id(id)
        if cars_data: 
            return cars_schema.dump(cars_data)
        