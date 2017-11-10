from app import db

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String, unique=True)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def __init__(self, username, password, name, email):
		self.username = username
		self.password = password
		self.name = name
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username

class Texto(db.Model):
	__tablename__ = "textos"

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(20))
	texto = db.Column(db.String(1000))
	coautores = db.Column(db.String(80))
	descricao = db.Column(db.String(200))
	autor = db.Column(db.String(70))

	def __init__(self, titulo, texto, coautores, descricao, autor):
		self.titulo = titulo
		self.texto = texto
		self.coautores = coautores
		self.descricao = descricao
		self.autor = autor

	def __repr__(self):
		return '<Texto %r>' % self.id

class Comentario(db.Model):
	__tablename__ = "comentarios"

	id = db.Column(db.Integer, primary_key=True)
	post_id = db.Column(db.Integer, db.ForeignKey('textos.id'))
	comentario = db.Column(db.Text)

	posts = db.relationship('Texto', foreign_keys=post_id)

	def __init__(self, post_id, comentario):
		self.post_id= post_id
		self.comentario = comentario

	def __repr__(self):
		return '<Comentario %r>' % self.id

	
