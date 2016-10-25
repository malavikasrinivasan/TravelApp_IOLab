from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired
import sqlite3 as sql

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class TripForm(Form):
    trip_name = StringField('Name of Trip', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    friends = SelectField('Bring a Friend')

    def get_friends(self):
        with sql.connect("app.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            result = cur.execute("select username from users").fetchall()
            friends = [(user['username'], user['username']) for idx, user in enumerate(result)]
            self.friends.choices = friends

