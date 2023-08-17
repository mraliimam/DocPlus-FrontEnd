from flask import render_template, redirect, url_for, flash, request, send_file
from market import app




@app.route('/login', methods = ['GET', 'POST'])
def login_page():
     return render_template('login.html')



@app.route('/')
@app.route('/home')
def home_page():    
    return render_template('home.html')

@app.route('/pharmacy/medicine', methods = ['GET', 'POST'])
def med_page():
    pass

@app.route('/form', methods = ['GET', 'POST'])
def form_page():
    pass



@app.route('/<category>', methods = ['GET', 'POST'])
def reception_page(category):
    return render_template('reception.html')


    

@app.route('/financials/category', methods = ['GET','POST'])
def financials_page():
    pass

@app.route('/financials/reports', methods = ['GET'])
def finReport_page():
    pass

@app.route('/<name>/patients', methods = ['GET', 'POST'])
def patient_page(name):
    pass


@app.route('/reception/checkout', methods = ['GET','POST'])
def bill_page():
    pass




@app.route('/swmc/<name>', methods = ['GET', 'POST'])
def swmc_page(name):
    pass

@app.route('/patient/editForm', methods = ['GET', 'POST'])
def patient_edit():
    pass


@app.route('/pharmacy/add-medicne', methods = ['GET', 'POST'])
def pharm_page():
    pass
@app.route('/patient/reports', methods = ['GET', 'POST'])
def reports_page():
    pass

@app.route('/laboratory/labs', methods = ['GET', 'POST'])
def lab_page():
    pass

@app.route('/laboratory/labs/viewFile')
def view_lab_file():
    pass
@app.route('/expenseForm', methods = ['GET','POST'])
def expense_page():
    pass

@app.route('/home/admin/freePatients')
def free_patients():
    pass
