from flask import render_template, redirect, url_for, flash, request, send_file
from market import app




@app.route('/login', methods = ['GET', 'POST'])
def login_page():
     return render_template('login.html')



@app.route('/')
@app.route('/home')
def home_page():    
    return render_template('home.html')


@app.route('/form', methods = ['GET', 'POST'])
def form_page():
    return render_template('form.html')


@app.route('/reception', methods = ['GET', 'POST'])
def reception_page():
    return render_template('reception.html')

@app.route('/patient_list', methods = ['GET', 'POST'])
def swmc_patient_list():
    return render_template('swmc.html')

@app.route('/editForm', methods = ['GET', 'POST'])
def edit_form():
    return render_template('pData.html')

@app.route('/financialscategory', methods = ['GET','POST'])
def financials_page():
    arr=[]
    return render_template('financials.html',arr=arr)

@app.route('/medicine', methods = ['GET', 'POST'])
def med_page():
    return render_template('medform.html')

@app.route('/financials/reports', methods = ['GET'])
def finReport_page():
    pass

@app.route('/patient', methods = ['GET', 'POST'])
def patient_page():
    return render_template('patient.html')


#@app.route('/reception/checkout', methods = ['GET','POST'])
@app.route('/invoice', methods = ['GET','POST'])
def bill_page():
    return render_template('bill.html')


'''

@app.route('/swmc/<name>', methods = ['GET', 'POST'])
def swmc_page(name):
    pass
'''

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
    return render_template('expense.html')

@app.route('/homeadmin/freePatients')
def free_patients():
    return render_template('freePatient.html')

@app.route('/upload')
def upload_medicine():
    return render_template('upload.html')
