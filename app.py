from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Set up Flask
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waifu_database.db' # Creates waifu_database.db in current directory
db = SQLAlchemy(app)

# Input args
# Set mandatory parameters that must be passed for database commands
waifu_args = reqparse.RequestParser()
waifu_args.add_argument("name", type=str, help="Name of the waifu is required.", required=True)
waifu_args.add_argument("anime", type=str, help="Name of the waifu's anime is required.", required=True)
waifu_args.add_argument("rank", type=int, help="Rank of the waifu is required.", required=True)


class WaifuEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary_key=True makes id a unique identifier
    name = db.Column(db.String(100), nullable=False) # nullable=False means you must enter something
    anime = db.Column(db.String(200), nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    # Special class method used to represent class objects as a string
    # i.e. Returns Waifu() method as a string
    def __repr__(self):
        return f"Waifu(name = {name}, anime = {anime}, rank = {rank})"


class WaifuList(Resource):
    # For serializing returned class instances
    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "anime": fields.String,
        "rank": fields.Integer
    }

    @marshal_with(resource_fields)
    def post(self, waifu_id):
        '''
        POST is for adding new entries to the list/database.
        The description is made optional, with all else being mandatory.
        '''

        # Parse inputted args and create a new waifu entry
        args = waifu_args.parse_args()

        # Check if it's a repeat entry (for ID and name)
        id_result = WaifuEntry.query.filter_by(id=waifu_id).first()
        
        if id_result:
            abort(409, message="ID taken...")
        name_result = WaifuEntry.query.filter_by(name=args["name"]).first()
        if name_result:
            abort(409, message="Waifu already exists within database...")

        # Move all entries with ranks equal to or lower down by 1 to avoid tie ranks
        existing_results = WaifuEntry.query.filter(WaifuEntry.rank >= args["rank"]).all()
        for res in existing_results:
            res.rank += 1
        
        # Finally, add new entry
        waifu = WaifuEntry(id=waifu_id, name=args["name"], anime=args["anime"], rank=args["rank"])

        # Commit addition (and changes) to database
        db.session.add(waifu)
        db.session.commit()

        # Remember to return only JSONs!
        # No strings, no ints, no JSON + strings!!!
        return waifu


if __name__ == "__main__":
    # Create database
    db.create_all()

    # Add the Resource class as an API accessible through the given endpoint (i.e. "/waifulist")
    api.add_resource(WaifuList, "/waifulist/<int:waifu_id>")

    # Run app
    app.run(debug=True)



