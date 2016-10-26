from flask import render_template, redirect, request, session, url_for, escape
from app import app, models, db
from .forms import LoginForm, TripForm
# Access the models file to use SQL functions


@app.route('/')
def index():
    username = ''
    if 'username' in session:
        username = session['username']
        trips = models.get_trips(username)
        return render_template('trips.html', name=username, trips=trips)
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

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    form = TripForm()
    if form.validate_on_submit():
        trip_name = form.trip_name.data
        destination = form.destination.data
        username = session['username']
        friend = form.friend.data
        # print(trip_name, destination, friend)
        models.insert_trip(trip_name,destination,username,friend) 
        return redirect('/trips')
    return render_template('create_trip.html', form=form)

@app.route('/trips')
def trips():
    username = session['username']
    # TODO: display all trips
    trips = models.get_trips(username)
    print(trips)
    return render_template('trips.html', name=username, trips=trips)

@app.route('/create_trip_button')
def create_trip_button():
    return redirect(url_for('create_trip'))

@app.route('/remove/<value>', methods=['GET', 'POST'])
def remove(value):
    form = TripForm()
    models.remove_trip(value)
    return redirect('/trips')
    # return render_template('trips.html', form=form)