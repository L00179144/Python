"""
Author : Raghul Gopalakrishnan
Contact : raghulgk@gmail.com
Purpose : Tutorials and demonstration for loops and statements in python programming
Pre-requisites : Python3 installation.
"""

mark = 78


#if and else
if(mark>=50) :
    result = "pass"
else :
    result = "fail"
print (result)

#if else and elif
if(mark<50) :
    result = "fail"
elif (mark<70) :
    result = "below average"
elif(mark<90) :
    result = "above average"
else :
    result = "excellent"

print (result)


#for loop 
    
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for items in array :
    if(items % 2 == 0):
        print(f"{items} is even")


scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}

#while loop

x = 100
while x>50:
    print(f"x now is {x}")
    x= x-1
else:
    print("x is now lesser than 50")








