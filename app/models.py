from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    type = db.Column(db.String(80))
    no_bedrooms = db.Column(db.String(80))
    no_bathrooms = db.Column(db.String(80))
    location = db.Column(db.String(128))
    price = db.Column(db.String(128))
    description = db.Column(db.String(256))
    image_name = db.Column(db.String(256)) 

    def __init__(self, title, type, no_bedrooms, no_bathrooms, location, price, description, image_name):  
        self.title = title
        self.type = type
        self.no_bedrooms = no_bedrooms
        self.no_bathrooms = no_bathrooms
        self.location = location
        self.price = price
        self.description = description
        self.image_name = image_name  

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  
        except NameError:
            return str(self.id)  

    def __repr__(self):
        return f"<Property {self.title}>"
