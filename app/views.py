"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import NewProperty
from .models import Property
from app import app, db
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property/create', methods=['POST','GET'])
def addProperty():
    form = NewProperty()
    if form.validate_on_submit():
        # Process the form data
        title = form.title.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        price = form.price.data
        property_type = form.property_type.data
        description = form.description.data
        photo = form.photo.data
        new_property = Property(
            title=title,
            type = property_type,
            no_bedrooms=bedrooms,
            no_bathrooms=bathrooms,
            location=location,
            price=price,
            description=description,
            image_name=photo.filename  # Assuming you want to store the filename in the database
        )
        
        # Add the new property to the database session
        db.session.add(new_property)
        db.session.commit()
        
        flash('You have successfully added a new property', 'success')
        return redirect(url_for('properties'))
    flash_errors(form)
    return render_template('newProperty.html', form=form)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
