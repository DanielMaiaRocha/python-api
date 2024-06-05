from db import db

class clientModel(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(80), nullable = False, unique = True)
    Email = db.Column(db.String(80), nullable = False,)
    Password = db.Column(db.String(80), nullable = False,)
    
    def __init__(self, Name, Email, Password):
        self.Name = Name
        self.Email = Email
        self.Password = Password
    
    def __repr__(self, ):
        return f'clientModel(Name={self.Name}, Email={self.Email}, Password={self.Password})'
    
    def json(self, ):
        return {
            'Name': self.Name,
            'Email': self.Email,
            'Password': self.Password,
        }
    
    @classmethod
    def find_by_title(cls, Name):
        return cls.query.filter_by(Name=Name).first()
    
    @classmethod 
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod 
    def find_by_email(cls, email):
        return cls.query.filter_by(Email=email).first()
    
    @classmethod
    def check_password(self, provided_password):
        return self.password == provided_password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit() 
            
        