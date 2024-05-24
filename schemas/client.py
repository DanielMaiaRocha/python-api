from ma import ma
from models.client import clientModel
from marshmallow import ValidationError, validates

class clientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = clientModel
        load_instance = True
    @validates('Password')
    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long')    