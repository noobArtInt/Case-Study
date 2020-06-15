from src import app
from flask import render_template, request
from src.forms import LoginForm, CustomerForm
from src.dbase import Newcustomer, db

@app.route('/', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template("login.html",title ="Create Customer", form=form, login=True)

@app.route('/create-customer',methods=['GET','POST'])
def createcustomer():
    form = CustomerForm()
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
            try:
            	date = datetime.now()
            except:
            	date = 0
            context={'ssnid':ssnid, 'name':name , 'age':age, 'address':address, 'state':state, 'city':city}

            entry = Newcustomer(ssnid=ssnid,name=name,age=age,address=address,state=state,city=city,date=date )
            db.session.add(entry)
            db.session.commit()
            flash(success_msg)
            form = CustomerForm()
    return render_template('create-customer.html',error=error, form=form)