from db import db

class carsModel(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False, unique = True)
    pages = db.Column(db.Integer, nullable = False,)
    
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __repr__(self, ):
        return f'carsModel(title={self.title}, pages={self.pages})'
    
    def json(self, ):
        return {
            'title': self.title,
            'pages': self.pages
        }
    
    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
    
    @classmethod 
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        de.session.commit() 
        
        