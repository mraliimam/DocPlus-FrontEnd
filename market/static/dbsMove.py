from market import db
from flask import send_file
import pandas as pd
from datetime import date

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def emails():
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = 'salhadwelfarefoundation@gmail.com'
    msg['To'] = 'hafizaliimam@gmail.com'
    msg['Subject'] = 'SWMC Database Excel File' + str(date.today())

    # Open the Excel file in binary mode
    with open('output.xlsx', 'rb') as f:
        # Add the Excel file as an attachment
        part = MIMEBase('application', "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='output.xlsx')
        msg.attach(part)

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587) # or use smtp.gmail.com for gmail
    server.starttls()
    server.login('salhadwelfarefoundation@gmail.com', 'Anees777')
    server.sendmail('salhadwelfarefoundation@gmail.com', 'hafizaliimam@gmail.com', msg.as_string())
    server.quit()
    
    return 'Pass'


def dbs2excel():

    # List of tables to export
    tables = ['Medicine', 'Patient_List', 'Patient_Data', 'Expense', 'Labs']

    writer = pd.ExcelWriter('market/database/output.xlsx', engine='openpyxl')

    # Iterate through the list of tables
    for table in tables:
        # Execute a SELECT * query to retrieve all data from the table
        # result = db.engine.execute(f"SELECT * FROM {table}")

        if table == 'Patient_Data':
            result = db.engine.execute('''SELECT pd.id, pd.MRN, p.Name, pd.Visited as Date, pd.Type_of_Service,d.Name
                                         as Doctor,pd.Prescription, pd.Notes, lb.Labs, pd.Blood_Pressure, pd.Temperature,
                                         pd.Saturation, p.Free, f.Laboratory, f.Medicine from patient_data pd 
                                         join doctor d on d.id = pd.doctor join Fee f on f.id = pd.id join patient_list p 
                                         on p.MRN = pd.MRN left join(SELECT group_concat(lab_name) as Labs,patient_id
                                        from patient_lab group by patient_id) as lb on lb.patient_id = pd.id; ''')

        elif table == 'Labs':
            result = db.engine.execute('select * from labs where Status = "OUT";')
        
        else:
            result = db.engine.execute(f'select * from {table}')

        # Convert the result to a DataFrame
        df = pd.DataFrame(result.fetchall(),columns=result.keys())
        # df.columns = result.keys()

        # Export the DataFrame to a new sheet in the Excel file
        df.to_excel(writer, sheet_name=table, index=False)

    # Save the Excel file
    writer.save()

    try:
        return send_file('database/output.xlsx', download_name='output.xlsx', as_attachment=False)
    except:
        return "Fail"
    
    
    # if emails() == 'Pass':

    #     return "Pass"

    # else:
    #     return "Fail"
