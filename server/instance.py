from flask import Flask, Blueprint
from flask_restx import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='Vip Colection')
        self.app.register_blueprint(self.blueprint)
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPETIONS'] = True 
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
        
        self.cars_ns = self.cars_ns()
        
    def cars_ns(self, ):
        return self.api.namespace(name='Cars', description='cars related operation', path='/')
        
    def run(self, ):
        self.app.run(
            port=5000,
            debug= True,
            host= '0.0.0.0'
        )
            
server = Server()