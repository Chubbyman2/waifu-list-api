# waifu-list-api

## Introduction
I'm tired of continuously updating my waifu list Google Doc, so I've decided to make it into a REST API that can be accessed by others, along with an independent website for everyone to see. The API allows for the GET, POST, PUT, and DELETE methods, with the latter three requiring the appropriate password to be inputted as a parameter. For more details, see <a href="https://github.com/Chubbyman2/waifu-list-api/blob/main/test.py">```test.py```</a>.

## Getting Started
To get started, clone the repo and make the following alterations:
* app.py: Change BASE variable assignment to local host
* api.py: Change PASSWORD variable assignment to anything you want
* test.py: Change BASE and PASSWORD to what you set previously

### Prerequisites
```
certifi==2022.5.18.1
charset-normalizer==2.0.12
click==8.1.3
colorama==0.4.4
Flask==2.1.2
greenlet==1.1.2
idna==3.3
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
requests==2.28.0
SQLAlchemy==1.4.37
urllib3==1.26.9
Werkzeug==2.1.2
```

## Built With
### Flask-RESTful
An extension for Flask that adds support for quickly building REST APIs. Comes and is used in conjunction with Flask. 

### SQLAlchemy 
Used for creating the mySQL database, as well as sending HTTP methods for the REST API. 

### SQLite3
Since you can't call an API inside of the API itself, I used SQLite3 to retrieve the waifu entries from the database to display on the front end.

## License
This project is licensed under the MIT License - see the <a href="https://github.com/Chubbyman2/waifu-list-api/blob/main/LICENSE">LICENSE</a> file for details.
