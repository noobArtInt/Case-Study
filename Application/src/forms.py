from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect, CSRFError

class LoginForm(FlaskForm):
	user = StringField("Username", validators=[DataRequired(), Length(min=8)])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=10)])
	submit = SubmitField("Login")
	print(user, password)

