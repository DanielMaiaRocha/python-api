from ma import ma
from models.cars import carsModel

class CarsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = carsModel
        load_instace = True