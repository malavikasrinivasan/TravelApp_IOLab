import sqlite3 as sql

def insert_customer(company,email):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO customers (company,email) VALUES (?,?)", (company,email))
        con.commit()

