from flask import Flask,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

from . import routes

