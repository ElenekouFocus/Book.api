# Book.api
Full Stack Book.api
Getting Started
# Installing Dependencies
python 3.10.0
pip 22.1.2 from C:\Users\justy\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
Follow instructions to install the latest version of python for your platform in the python docs

# Virtual Environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

# PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /Book.api directory and running:

pip install -r requirements.txt
or
pip3 install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.
Key Dependencies
 •app.py is a lightweight backend microservices framework. Flask is required to handle requests and responses.
 •SQLAlchemy is the Python SQL toolkit and ORM we’ll use handle the lightweight sqlite database. You’ll primarily work in app.py and can reference auth.py.
 •app-CORS is the extension we’ll use to handle cross origin requests from our frontend server.
# Database Setup
With Postgres running, restore a database using the api_database.sql file provided. From the backend folder in terminal run:
psql api_database < api_database.sql
Running the server
From within the Book_api directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run

To run the server on Windows, execute:

set FLASK_APP=app.py
set FLASK_ENV=development
flask run
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the init.py file to find the application

# API REFERENCE
Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

# Error Handling
Errors are retourned as JSON objects in the following format: { “success”:False “error”: 400 “message”:"Bad request }

The API will return four error types when requests fail: . 400: Bad request . 500: Internal server error . 422: Unprocessable . 404: Not found

# Endpoints
. ## GET/books

# GENERAL:
This endpoints returns a list of book object, success value, total number of the books.

SAMPLE: curl http://localhost:5000/livres

{
  "livres": [
    {
      "categorie_id": 1, 
      "date_parution": "Tue, 05 Sep 1505 00:00:00 GMT", 
      "editeur": "Gil", 
      "id": 3, 
      "isbn": "PM", 
      "titre": "Le corps animal", 
      "version": "2.1"
    }, 
    {
      "categorie_id": 1, 
      "date_parution": "Wed, 10 Feb 2016 00:00:00 GMT", 
      "editeur": "bertin", 
      "id": 4, 
      "isbn": "PA", 
      "titre": "Corps humain", 
      "version": "1.0.1"
    }, 
    {
      "categorie_id": 1, 
      "date_parution": "Sun, 10 Feb 2019 00:00:00 GMT", 
      "editeur": "bertin0", 
      "id": 5, 
      "isbn": "PA", 
      "titre": "Corps humain", 
      "version": "1.0.2"
    }
  ], 
  "nombres_livres": 3
}

SAMPLE: curl http://localhost:5000/categories

 "categories": [
        {
            "description_categorie": "Biolo",
            "id": 1,
            "libelle_categorie": "SA"
        },
        {
            "description_categorie": "Tous ce qui nous entour",
            "id": 4,
            "libelle_categorie": "Sciences Environnementale"
        },
        {
            "description_categorie": "Etude de la litterature",
            "id": 5,
            "libelle_categorie": "livres litteraires"
        },
        {
            "description_categorie": "Etude de la politique",
            "id": 6,
            "libelle_categorie": "livres geopolitiques"
        }
    ],
    "nombre_categorie": 4
}
. ## DELETE/livres (livre_id)

    GENERAL:
        Delete the book of the given ID if it exists. Return the id of the deleted livre, success value, total of books a

        Results are paginated in groups of 10. include a request argument to choose page number, starting from 1.

        SAMPLE: curl -X DELETE http://localhost:5000/livres/3

{
  "livres": [ 
    {
      "categorie_id": 1, 
      "date_parution": "Wed, 10 Feb 2016 00:00:00 GMT", 
      "editeur": "bertin", 
      "id": 4, 
      "isbn": "PA", 
      "titre": "Corps humain", 
      "version": "1.0.1"
    }, 
    {
      "categorie_id": 1, 
      "date_parution": "Sun, 10 Feb 2019 00:00:00 GMT", 
      "editeur": "bertin0", 
      "id": 5, 
      "isbn": "PA", 
      "titre": "Corps humain", 
      "version": "1.0.2"
    }
  ], 
  "nombres_livres": 2
}

. ##PATCH/livres(livre_id)
  GENERAL:
  This endpoint is used to update a primary_color of book
  We return a book which we update

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/livres/4 -H "Content-Type:application/json" -d "{"editeur":"Ablavi"}"
{
    "categorie_id": 1, 
    "date_parution": "Wed, 10 Feb 2016 00:00:00 GMT", 
    "editeur": "Ablavi", 
    "id": 4, 
    "isbn": "PA", 
    "titre": "Corps humain", 
    "version": "1.0.1"
},

. ## POST/plants

  GENERAL:    
  This endpoint is used to create a new book or to search for a  book in relation to the terms contained in the  books.
  When the searchTerm parameter is passed from the json, the endpoint performs the search. Otherwise, it is the creation of a new question.
  In the case of the creation of a new question:
  We return the ID of the new book created, the book that was created, the list of  book and the number of  books.

  SAMPLE.....For Search:
  curl -X POST http://localhost:5000/livres -H "Content-Type:application/json" -d "{"search":"title"}"

  SAMPLE.....For create

  curl -X POST http://localhost:5000/livres -H "Content-Type:application/json" -d "{"isbn": "PM","titre": "Le corps animal","date_parution": "Tue, 05 Sep 1505 00:00:00 GMT","editeur": "Gillos","version": "2.1","categorie_id": 2,}"

{
  "livres": [ 
    {
      "categorie_id": 1, 
      "date_parution": "Wed, 10 Feb 2016 00:00:00 GMT", 
      "editeur": "bertin", 
      "id": 4, 
      "isbn": "PA", 
      "titre": "Corps humain", 
      "version": "1.0.1"
    }, 
    {
      "categorie_id": 1, 
      "date_parution": "Sun, 10 Feb 2019 00:00:00 GMT", 
      "editeur": "bertin0", 
      "id": 5, 
      "isbn": "PA", 
      "titre": "Corps humain", 
      "version": "1.0.2"
    },
    {
      "categorie_id": 2, 
      "date_parution": "Tue, 05 Sep 1505 00:00:00 GMT", 
      "editeur": "Gillos", 
      "id": 6, 
      "isbn": "PM", 
      "titre": "Corps animal", 
      "version": "2.1"
    }
  ], 
  "nombres_livres": 3
}
. ## POST/categories

  GENERAL:    
  This endpoint is used to create a new categorie or to search for a categorie in relation to the terms contained in the categories.
  When the searchTerm parameter is passed from the json, the endpoint performs the search. Otherwise, it is the creation of a new question.
  In the case of the creation of a new question:
  We return the ID of the new categorie created, the book that was created, the list of  book and the number of  categories.

  SAMPLE.....For Search:
  curl -X POST http://localhost:5000/categories -H "Content-Type:application/json" -d "{"search":"title"}"

  SAMPLE.....For create

  curl -X POST http://localhost:5000/livres -H "Content-Type:application/json" -d "{"libelle_categorie": "Sciences geopolitiquee", "description_categorie": "Tous ce qui concerne la politique"}"
{
    "categorie_id": 7,
    "categories": [
        {
            "description_categorie": "Biolo",
            "id": 1,
            "libelle_categorie": "SA"
        },
        {
            "description_categorie": "Tous ce qui nous entour",
            "id": 4,
            "libelle_categorie": "Sciences Environnementale"
        },
        {
            "description_categorie": "Etude de la litterature",
            "id": 5,
            "libelle_categorie": "livres litteraires"
        },
        {
            "description_categorie": "Etude de la politique",
            "id": 6,
            "libelle_categorie": "livres geopolitiques"
        },
        {
            "description_categorie": "Tous ce qui concerne la politique",
            "id": 7,
            "libelle_categorie": "Sciences geopolitiquee"
        }
    ],
    "nombre_categories": 5
}
## Testing
To run the tests, run
dropdb api createdb api psql api_test < api.sql python test_app.py





              



              
