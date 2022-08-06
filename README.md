# Book.api

Toggle Mode
  
Full Stack Book.api
Getting Started
Installing Dependencies
python 3.10.0
pip 22.1.2 from C:\Users\justy\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
Follow instructions to install the latest version of python for your platform in the python docs

Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /Book.api directory and running:

pip install -r requirements.txt
or
pip3 install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.
Key Dependencies
• Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.
•SQLAlchemy is the Python SQL toolkit and ORM we’ll use handle the lightweight sqlite database. You’ll primarily work in app.py and can reference auth.py.
•Flask-CORS is the extension we’ll use to handle cross origin requests from our frontend server.
Database Setup
With Postgres running, restore a database using the api_database.sql file provided. From the backend folder in terminal run:
psql api_database < api_database.sql
Running the server
From within the Book_api directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

To run the server on Windows, execute:

set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the init.py file to find the application

API REFERENCE
Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

Error Handling
Errors are retourned as JSON objects in the following format: { “success”:False “error”: 400 “message”:"Bad request }

The API will return four error types when requests fail: . 400: Bad request . 500: Internal server error . 422: Unprocessable . 404: Not found

Endpoints
. ## GET/books

GENERAL:
This endpoints returns a list of book object, success value, total number of the books.

SAMPLE: curl http://localhost:5000/books
{
“livres”: [
{
“categorie_id”: 1,
“date_parution”: “Tue, 05 Sep 1505 00:00:00 GMT”,
“editeur”: “Gil”,
“id”: 3,
“isbn”: “PM”,
“titre”: “Le corps animal”,
“version”: “2.1”
}
],
“nombres_livres”: 1
}
