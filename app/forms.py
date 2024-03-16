from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField,FileRequired,FileAllowed


class NewProperty(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    bedrooms = StringField('No. of Rooms', validators=[InputRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Upload Image', validators=[
        FileRequired(message='Browse'),
        FileAllowed(['jpg', 'png'], message='Only JPEG and PNG images are allowed.')
    ])