import sqlite3
from api import db, WaifuList
from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# Set up Flask
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waifu_database.db' # Creates waifu_database.db in current directory
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
    con = sqlite3.connect("waifu_database.db")
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
    



