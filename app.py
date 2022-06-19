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

# Heroku ver
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://mmebfnoddiyfdu:a27e7922b693819e741fab27a8ef7dae6333223331f797e86c0d6158d65a2a72@ec2-52-71-23-11.compute-1.amazonaws.com:5432/df1o6v6ncitvl4"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sql5500726:whE69C32BV@sql5.freesqldatabase.com/sql5500726?charset=utf8mb4"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Just to get rid of that annoying warning message
db.init_app(app) # To avoid circular import
db = SQLAlchemy(app) # Bind to app after creation in api.py
# BASE = "http://127.0.0.1:5000/"
BASE = "https://waifu-list-api.herokuapp.com"


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
    cur = con.cursor()
    cur.execute("SELECT * from waifu_entry")
    waifus = cur.fetchall()

    return waifus


if __name__ == "__main__":
    # Create database
    db.create_all()

    # Add the Resource class as an API accessible through the given endpoint (i.e. "/waifulist")
    api.add_resource(WaifuList, "/waifulist")

    # Run app
    app.run(debug=True)
