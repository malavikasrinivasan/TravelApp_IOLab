import sqlite3 as sql

def get_users():
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row # Convert rows into a dictionary format
        cur = con.cursor()
        result = cur.execute("select * from users").fetchall()
        return result
