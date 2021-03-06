# waifu-list-api

## Introduction
I'm tired of continuously updating my waifu list Google Doc, so I've decided to make it into a REST API that can be accessed by others, along with an independent website for everyone to see. The API allows for the GET, POST, PUT, and DELETE methods, with the latter three requiring the appropriate password to be inputted as a parameter. For more details, see <a href="https://github.com/Chubbyman2/waifu-list-api/blob/main/test.py">```test.py```</a>. That being said, may I present: My <a href="https://waifu-list-api.herokuapp.com/">waifu-list-api</a>!

## Getting Started
To get started locally, clone the repo and make the following alterations:
* app.py: Change BASE variable assignment to local host and app.config to the sqlite db. Also change pymysql to sqlite3 accordingly.
* api.py: Change PASSWORD variable assignment to anything you want
* demo.py: Change BASE and PASSWORD to what you set previously

### Prerequisites
```
aniso8601==8.0.0
certifi==2022.5.18.1
charset-normalizer==2.0.12
click==7.1.2
colorama==0.4.4
Flask==1.1.2
Flask-RESTful==0.3.8
Flask-SQLAlchemy==2.4.3
greenlet==1.1.2
gunicorn==20.1.0
idna==3.3
importlib-metadata==4.11.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
psycopg2==2.9.3
PyMySQL==1.0.2
pytz==2020.1
requests==2.28.0
six==1.15.0
SQLAlchemy==1.3.18
urllib3==1.26.9
Werkzeug==1.0.1
wincertstore==0.2
zipp==3.8.0
```

### Deploying Locally
Set to correct project directory:
```cd waifu-list-api```

With virtual environment:
```python app.py```

Then, using a separate command terminal:
```python demo.py```

### Integrating with Local Scripts
<a href="https://github.com/Chubbyman2/waifu-list-api/blob/main/demo.py">```demo.py```</a> provides a bunch of helper functions for easily communicating with the REST API, without you having to learn requests or HTTP methods. Just make sure to know your API base path (BASE) and password (PASSWORD). 

## Built With
### Flask-RESTful
An extension for Flask that adds support for quickly building REST APIs. Comes and is used in conjunction with Flask. 

### SQLAlchemy 
Used for creating the mySQL database, as well as sending HTTP methods to the REST API. 

### SQLite3/PyMySQL
Since you can't call an API inside of the API itself, I used SQLite3 to retrieve the waifu entries from the database to display on the front end. Since I'm storing the waifus using a remote database, I had to switch to PyMySQL for the deployed version.

### Heroku
THIS TOOK WAY LONGER THAN EXPECTED. Deployment is so annoying, I swear... Anyways, the API endpoint and home page are hosted using Heroku, while the SQL database is hosted using Heroku's provided ClearDB MySQL. I had to fix this since FreeSQLDatabase.com only provides a trial period...

## License
This project is licensed under the MIT License - see the <a href="https://github.com/Chubbyman2/waifu-list-api/blob/main/LICENSE">LICENSE</a> file for details.
