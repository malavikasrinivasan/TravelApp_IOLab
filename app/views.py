from flask import render_template, redirect, request
from app import app, models, db
from .forms import 
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')


@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
        # Get data from the form
        # Send data from form to Database
    form = OrderForm()
    if form.validate_on_submit():
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        models.insert_orders(name_of_part, manufacturer_of_part, value)
        return redirect('/customers')
    return render_template('orders.html', form=form)
