import sqlite3 as sql

# Write and Read from and to database

##You might have additional functions to access the database
def get_users():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row # Convert rows into a dictionary format
        cur = con.cursor()
        result = cur.execute("select * from users").fetchall()
        return result
