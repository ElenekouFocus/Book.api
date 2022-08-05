from flask_bootstrap import Bootstrap
from ensurepip import version
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from auth import requires_auth
motdepasse = os.getenv('motdepasse')
app = Flask(__name__)
Bootstrap(app)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost:5432/api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,PATCH,DELETE,OPTIONS')
    return response


class Livre(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(50), nullable=False)
    titre = db.Column(db.String(100), nullable=False)
    date_parution = db.Column(db.Date, nullable=False)
    editeur = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)

    def __init__(
        self,
        isbn,
        titre,
        date_parution,
        editeur,
        version,
        categorie_id
    ):
        self.isbn = isbn
        self.titre = titre
        self.date_parution = date_parution
        self.editeur = editeur
        self.version = version
        self.categorie_id = categorie_id

    def format(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date_parution': self.date_parution,
            'editeur': self.editeur,
            'version': self.version,
            'categorie_id': self.categorie_id,
        }


class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(100), nullable=False)
    description_categorie = db.Column(db.String(100), nullable=False)
    livres = db.relationship(
        'Livre', backref=db.backref('categories', lazy=True)
    )

    def format(self):
        return {
            'id': self.id,
            'libelle_categorie': self.libelle_categorie,
            'description_categorie': self.description_categorie,
        }
# listes des livres


@app.route('/livres')
@requires_auth('get:livres')
def liste_libre(payload):
    livres = Livre.query.all()
    return jsonify({
        'nombres_livres': len(livres),
        'livres': [livre.format() for livre in livres]
    })
# Recuperer un livre


@app.route('/livres/<int:id>')
@requires_auth('get:livres')
def get_livre(id,payload):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return jsonify({
            'id': id,
            'livre': livre.format()
        })
# Ajouter un livre


@app.route('/livres', methods=['POST'])
@requires_auth('get:livres')
def Ajouter_livre(payload):
    body = request.get_json()
    new_isbn = body.get('isbn', None)
    new_titre = body.get('titre', None)
    new_date_parution = body.get('date_parution', None)
    new_editeur = body.get('editeur', None)
    new_version = body.get('version', None)
    new_categorie_id = body.get('categorie_id', None)
    if not (new_isbn or new_titre or new_date_parution or new_editeur or new_version, new_categorie_id):
        abort(400)
    else:
        livre = Livre(isbn=new_isbn, titre=new_titre,
                      date_parution=new_date_parution, editeur=new_editeur, version=new_version, categorie_id=new_categorie_id)
        db.session.add(livre)
        db.session.commit()
        livres = Livre.query.all()
        return jsonify({
            'livres': [livre.format() for livre in livres],
            'nombre_livres': len(livres),
        })
# modifier un livre


@app.route('/livres/<int:id>', methods=['PATCH'])
@requires_auth('get:livres')
def update_filiere(id,payload):
    livre = Livre.query.get(id)
    body = request.get_json()
    new_isbn = body.get('isbn', None)
    new_titre = body.get('titre', None)
    new_date_parution = body.get('date_parution', None)
    new_editeur = body.get('editeur', None)
    new_version = body.get('version', None)
    new_categorie_id = body.get('categorie_id', None)
    if livre is None:
        abort(400)
    livre.isbn = new_isbn,
    livre.titre = new_titre,
    livre.date_parution = new_date_parution,
    livre.editeur = new_editeur,
    livre.version = new_version,
    livre.categorie_id = new_categorie_id
    db.session.commit()
    return jsonify({
        'livre_id': id,
        'livre': livre.format()
    })
# Suprimmer un livre


@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_livre(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        db.session.delete(livre)
        db.session.commit()
        livres = Livre.query.all()
        return jsonify({
            'Livres': [livre.format() for livre in livres]
        })
# Listes des livres d'une categorie donnée


@app.route('/categories/<int:id>/livres')
def get_livres_by_categorie(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(400)
    else:
        livres = Livre.query.filter(Livre.categorie_id == id)
        return jsonify({
            'id_categorie': id,
            'livres': [livre.format() for livre in livres],
        })

# Listes des categories


@app.route('/categories')
def liste_categorie():
    categories = Categorie.query.all()
    return jsonify({
        'nombre_categorie': len(categories),
        'categories': [categorie.format() for categorie in categories]
    })

# Ajouter une categorie


@app.route('/categories', methods=['POST'])
def Ajouter_categorie():
    body = request.get_json()
    new_libelle_categorie = body.get('libelle_categorie', None)
    new_description_categorie = body.get('description_categorie', None)
    if not (new_libelle_categorie and new_description_categorie):
        abort(400)
    else:
        categorie = Categorie(libelle_categorie=new_libelle_categorie,
                              description_categorie=new_description_categorie)
        db.session.add(categorie)
        db.session.commit()
        categories = Categorie.query.all()
        return jsonify({
            'categories': [categorie.format() for categorie in categories],
            'nombre_categories': len(categories),
            'categorie_id': categorie.id
        })
# Modifier une categorie


@app.route('/categories/<int:id>', methods=['PATCH'])
def update_categorie(id):
    categorie = Categorie.query.get(id)
    body = request.get_json()
    new_libelle_categorie = body.get('libelle_categorie', None)
    new_description_categorie = body.get('description_categorie', None)
    if categorie is None:
        abort(400)
    categorie.libelle_categorie = new_libelle_categorie
    categorie.description_categorie = new_description_categorie
    db.session.commit()
    return jsonify({
        'categorie_id': id,
        'categorie': categorie.format(),
    })
# supprimer une categorie


@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_categorie(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)
    db.session.delete(categorie)
    db.session.commit()
    categories = Categorie.query.all()
    return jsonify({
        'categories': [categorie.format() for categorie in categories]
    })
