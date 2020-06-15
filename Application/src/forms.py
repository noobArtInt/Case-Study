from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, IntegerField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect, CSRFError

class LoginForm(FlaskForm):
	user = StringField("Username", validators=[DataRequired(), Length(min=8)], render_kw={"placeholder": "Username"})
	password = PasswordField("Password", validators=[DataRequired(), Length(min=10)], render_kw={"placeholder": "Password"})
	submit = SubmitField("Login")

class CustomerForm(FlaskForm):
	ssnid = IntegerField("SSN id", validators=[DataRequired(), Length(min=8)], render_kw={"placeholder": "SSN id"})
	name = StringField("Name", validators=[DataRequired()], render_kw={"placeholder": "Name"})
	age = IntegerField("Age", validators=[DataRequired()], render_kw={"placeholder": "Age"})
	Address = StringField("Address",validators=[DataRequired()], render_kw={"placeholder": "Address"})
	submit = SubmitField("Register")