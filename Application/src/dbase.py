#connect localhost mysql(db name = cs)
from . import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cs'
db = SQLAlchemy(app)

class Newcustomer(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    ssnid = db.Column(db.String(11), unique=True, nullable=False)
    name = db.Column(db.String(15), unique=True, nullable=False)
    age = db.Column(db.String(3), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    state = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.String(120), unique=True, nullable=False)

