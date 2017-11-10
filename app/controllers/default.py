# coding=UTF-8
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from app import app, db, lm

from app.models.tables import User, Comentario, Texto
from app.models.forms import LoginForm, RegisterComentario, RegisterPost

@lm.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and user.password == form.password.data:
			login_user(user)
			flash("Logged in")
			return redirect(url_for("timeline"))
		else:
			flash("Invalid login")
	return render_template('login.html',
		                      form=form)

@app.route("/logout")
def logout():
	logout_user()
	flash("Logged out")
	return redirect(url_for("index"))

@app.route("/cadastrar")
def cadastrar():
	return render_template("cadastro.html")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		name = request.form.get("name")
		email = request.form.get("email")

		if username and password and name and email:
			p = User(username, password, name, email)
			db.session.add(p)
			db.session.commit()

	return redirect(url_for("cadastrado"))

@app.route("/cadastrado")
def cadastrado():
	return render_template("cadastrado.html")

@app.route("/publicar")
def publicar():
	form = RegisterPost()
	return render_template("publicarPost.html", form=form)

@app.route("/publicacoes", methods=['GET', 'POST'])
def publicacoes():
	form = RegisterPost()
	aul = current_user.username
	if request.method == "POST":
		titulo = request.form.get("titulo")
		texto = request.form.get("texto")
		coautores = request.form.get("coautores")
		descricao = request.form.get("descricao")
		autor = aul

		if titulo and texto and coautores and descricao and autor:
			i = Texto(titulo, texto, coautores, descricao, autor)
			db.session.add(i)
			db.session.commit()
		#return "<h2> Novo texto publicado!!! </h2>" 

	return redirect(url_for("publicado"))
	
@app.route("/publicado")
def publicado():
	return render_template("publicado.html")

@app.route("/timeline")
def timeline():
	texto = Texto.query.all()
	#idusuario = current_user.id
	#texto = Texto.query.filter_by(autor=idusuario)
	return render_template('timeline.html', texto=texto)

@app.route("/textoCompleto/<int:id>", methods=['GET','POST'])
def textocompleto(id):	
	textt = Texto.query.get(id)
	#user = User.query.get(textt.autor)

	titulo=textt.titulo
	#autores= "autor: " + user.username + ", coautores: " + textt.coautores 
	descricao= textt.descricao
	texto= textt.texto

	form = RegisterComentario()
	comentario = Comentario.query.all()
	#comentario = Comentario.query.filter_by(post_id=id)


	#if form.validate_on_submit():
		#new_Comentario = Comentario( post_id=id, comentario=form.comentario.data )
		#db.session.add(new_Comentario)
		#db.session.commit()
		

	if request.method == "POST":
		post_id = id
		comentario = request.form.get("comentario")
		
		if post_id and comentario :
			q = Comentario(post_id, comentario)
			db.session.add(q)
			db.session.commit()
			return "<h2> Comentário adicionado! </h2>"

	return render_template("textoCompleto.html", titulo=titulo, texto=texto, descricao=descricao, id=id, form=form, comentario=comentario)







