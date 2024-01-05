"""
Author : Raghul Gopalakrishnan
Contact : raghulgk@gmail.com
Purpose : Tutorials and demonstration for time in python programming
Pre-requisites : Python3 installation.
"""

import datetime


# Get the current time
today = datetime.datetime.now()
print(today)
# Get Unix time
unix_epoch_time = datetime.datetime.timestamp(today)
print(unix_epoch_time)

weekday = datetime.datetime.now().strftime("%A") 
print(weekday)

month = datetime.datetime.now().strftime("%B")
print(month)

# get the current date and time
now = datetime.datetime.now()
print(now)

# get current date
current_date = datetime.date.today()

print(current_date)

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)
