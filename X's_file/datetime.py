import datetime

x = datetime.datetime.now()
print(x)
data = {'3665935030': {'name': 'Desmond', 'dob': '31/21/21', 'bvn': '23456789', 'pin': '1234', 'bal': 185000}}
print(data['3665935030'])

import datetime
input()
day = datetime.datetime.strptime(date,"%d-%m-%Y").date()
print(day)