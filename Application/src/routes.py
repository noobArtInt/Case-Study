from src import app
from flask import render_template
from src.forms import LoginForm

@app.route('/', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template("login.html", form=form, login=True)