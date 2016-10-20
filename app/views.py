from flask import render_template, redirect, request, session, url_for, escape
from app import app, models, db
from .forms import LoginForm, TripForm
# Access the models file to use SQL functions


@app.route('/')
def index():
    username = ''
    if 'username' in session:
        username = escape(session['username'])
        return render_template('trips.html', name=username)
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # print(username, password)
        
        # Getting user and pwd info from the database
        users = models.get_users()
        users_dict = {} # Dictionary of users and passwords
        for idx, user in enumerate(users):
            users_dict[user[0]] = user[1]  #user[0] <- username, user[1] <- password

        # Checking if username exists in the dictionary. If exists, checking password matches
        if username in users_dict.keys():
            if users_dict[username] == password:
                print("success")
                session['username'] = username
                return redirect('/trips')
            else:
                print("Incorrect passwords")
                return render_template('login.html', form=form, msg="Invalid password")

        else:
            print("Invalid username")
            return render_template('login.html', form=form, msg="Invalid username")


    return render_template('login.html', form=form)

@app.route('/trips', methods=['GET', 'POST'])
def trips():
    username = session['username']
    return render_template('trips.html', name=username)
