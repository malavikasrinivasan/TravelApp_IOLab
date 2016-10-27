import sqlite3 as sql

def get_users():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row # Convert rows into a dictionary format
        cur = con.cursor()
        result = cur.execute("select * from users").fetchall()
        return result

def insert_trip(trip_name,destination,username,friend):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trips (trip_name,destination,username,friend) VALUES (?,?,?,?)", (trip_name,destination,username,friend))
        con.commit()

def get_trips(user): # For a user, return their trips
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        # for user, select trips
        sql_query = "select *  from trips where username = '" + user + "'"
        # print(sql_query)
        result = cur.execute(sql_query).fetchall()
        # print(result)
    return result
    
