import os
import pymysql
import sqlite3
from api import db, WaifuList
from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# Set up Flask
app = Flask(__name__)
api = Api(app)

# Local ver
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///waifu_database.db" # Creates waifu_database.db in current directory
# BASE = "http://127.0.0.1:5000/"

# Heroku ver
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URI"]
BASE = "https://waifu-list-api.herokuapp.com"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Just to get rid of that annoying warning message
db.init_app(app) # To avoid circular import
db = SQLAlchemy(app) # Bind to app after creation in api.py
db.create_all()

# Add the Resource class as an API accessible through the given endpoint (i.e. "/waifulist")
api.add_resource(WaifuList, "/waifulist")


# Home page
@app.route("/")
def index():
    return render_template("index.html", len=len(waifu_list()), waifus=waifu_list())


def waifu_list():
    '''
    Returns all the waifus in the database to be displayed on the frontend.
    Somewhat obviously, you cannot call the API from within the API.
    So I have to use a different method of accessing the database (sqlite3).
    '''
    
    con = pymysql.connect(
        host="sql5.freesqldatabase.com",
        database="sql5500726",
        user="sql5500726",
        password="whE69C32BV",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    # con = sqlite3.connect("waifu_database.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS waifu_entry (id INT PRIMARY KEY, name VARCHAR(255), anime VARCHAR(255), rank INT, image VARCHAR(255)")
    print("Table successfully created.")
    
    cur.execute("SELECT * from waifu_entry ORDER BY rank")
    waifus = cur.fetchall()
    cur.close()
    con.close()

    return waifus


if __name__ == "__main__":
    # Run app
    app.run(debug=True)
