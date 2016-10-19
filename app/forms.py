from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class TripForm(Form):
    trip_name = StringField('Name of Trip', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    friend = StringField('Bring a Friend', validators=[DataRequired()])
