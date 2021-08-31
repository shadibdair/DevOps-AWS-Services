# First Install (Pandas), (openpyxl):
    # pip3 install pandas
    # pip3 install openpyxk

import openpyxl # To read and write from EXCEL file.
import pandas as pd # Is most widely used for data science/data analysis and machine learning tasks.


data = pd.read_excel (r'/Users/shadibadir/Desktop/ScriptPython/Shifts_SRE.xlsx')
df = pd.DataFrame(data, columns= ['Date','SRE']) # Printed all the content below the column that you choosed.
df.loc[df['SRE'] == 'Shadi', 'Time'] = '7:00 - 15:00' # (loc) attribute access a group of rows and columns by label(s)
print (df)

print('-----\n')

excel_file = ['/Users/shadibadir/Desktop/ScriptPython/Shifts_SRE.xlsx'] # Specifying the path of the EXCEL file.

values = [] # An empty list where we're goning to append our values 

# Loop through each single file in our file list:
for file in excel_file:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['Sheet1']
    date_sre = worksheet['A2'].value
    time_sre = worksheet['B2'].value
    oncall_sre = worksheet['C2'].value
    number_sre = worksheet['D2'].value
    
    values.append(date_sre)
    values.append(time_sre)
    values.append(oncall_sre)
    values.append(number_sre)
    print(date_sre, [time_sre], [oncall_sre], [number_sre])