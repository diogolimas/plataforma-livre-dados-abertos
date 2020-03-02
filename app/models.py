from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db, login

class User(UserMixin, db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(200), index=True, unique=True)
	email = db.Column(db.String(200), index=True, unique=True)
	password_hash = db.Column(db.String(150))
	about_me = db.Column(db.String(300))
	nickname = db.Column(db.String(150))
	typeUser = db.Column(db.String(200))
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class Source(db.Model):
	__tablename__ = "sources"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), index=True, unique=True)
	sphere = db.Column(db.String(200), index=True)
	description = db.Column(db.String(800), index=True)
	officialLink = db.Column(db.String(300), index=True)
	datasetLink = db.Column(db.String(300), index=True)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	user = db.relationship('User', backref=db.backref('sources', lazy=True))

	def __repr__(self):
		return '<Source {}>'.format(self.title)

class Software(db.Model):
	__tablename__ = "softwares"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), index=True, unique=True)
	description = db.Column(db.String(800), index=True)
	downloadLink = db.Column(db.String(300), index=True)
	activeDevelopment = db.Column(db.String(200), index=True)
	license = db.Column(db.String(200), index=True)
	owner = db.Column(db.String(200), index=True)
	dateCreation = db.Column(db.String(300), index=True)
	dateRelease = db.Column(db.String(300), index=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	user = db.relationship('User', backref=db.backref('softwares', lazy=True))

	def __repr__(self):
		return '<Software {}>'.format(self.title)

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	palavraChave = db.Column(db.String(200), index=True)

	def __repr__(self):
		return '<Tag{}>'.format(self.palavraChave)

class Categoria(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	def __repr__(self):
		return '<Categoria {}>'.format(self.id)

class Favorito(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	gostei = db.Column(db.String(200), index=True)

	def __repr__(self):
		return '<Favorito {}>'.format(self.gostei)

class Comentario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.String(200), index=True)
	texto = db.Column(db.String(500), index=True)

	def __repr__(self):
		return '<Comentario {}>'.format(self.data)

class Denuncia(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	descricao = db.Column(db.String(500), index=True)
	tipo = db.Column(db.String(200), index=True)

	def __repr__(self):
		return '<Denuncia {}>'.format(self.tipo)
