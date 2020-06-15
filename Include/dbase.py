#import flask from Flask
from flask import Flask,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#make application using Flask
app = Flask(__name__)
app.secret_key = 'super secret key'
#connect localhost mysql(db name = cs)
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



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create-customer',methods=['GET','POST'])
def createcustomer():
    error = None
    success_msg = 'Data submitted successfully'
    if(request.method == 'POST'):
        if(request.form['ssnid']=="" or request.form['name']=="" or request.form['age']=="" or request.form['address']==""):
            error = 'invalid credentials (All fields are mandetory)'
        else:
            ssnid = request.form.get('ssnid')
            name = request.form.get('name')
            age = request.form.get('age')
            address = request.form.get('address')
            state = request.form.get('state')
            city = request.form.get('city')
            date = datetime.now()
            entry = Newcustomer(ssnid=ssnid,name=name,age=age,address=address,state=state,city=city,date=date )
            db.session.add(entry)
            db.session.commit()
            flash(success_msg)

    return render_template('create-customer.html',error=error)





app.run(debug=True)
