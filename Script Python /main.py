import openpyxl # To read and write from EXCEL file.

"""
import datetime
DAY, NIGHT = 1, 2
def check_time(time_to_check, MorningShift, EveningShift, NightShift):
    if MorningShift > EveningShift and MorningShift < NightShift:
        if time_to_check > MorningShift or time_to_check < EveningShift:
            return NIGHT, True
    elif MorningShift < off_time:
        if time_to_check > MorningShift and time_to_check < EveningShift:
            return DAY, True
    elif time_to_check == MorningShift:
        return None, True
    return None, False


MorningShift = datetime.time(7,15)
EveningShift = datetime.time(15,23)
NightShift = datetime.time(23,7)
timenow = datetime.datetime.now().time()
current_time = datetime.datetime.now().time()

when, matching = check_time(current_time, MorningShift, EveningShift)

if matching:
    if when == NIGHT:
        print("Night Time detected.")
    elif when == DAY:
        print("Day Time detected.")
"""





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