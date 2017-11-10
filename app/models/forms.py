from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField ("password", validators=[DataRequired()])
	remember_me = BooleanField("remember_me")

class RegisterPost (Form):
	titulo = StringField("titulo", validators=[DataRequired()])
	texto = StringField ("texto", validators=[DataRequired()])
	coautores = StringField("coautores", validators=[DataRequired()])
	descricao = StringField("descricao", validators=[DataRequired()])
	autor = StringField("autor", validators=[DataRequired()])

class RegisterComentario(Form):
	comentario = StringField("comentario", validators=[DataRequired()])

