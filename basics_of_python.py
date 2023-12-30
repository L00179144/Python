"""
Author : Raghul Gopalakrishnan
Contact : raghulgk@gmail.com
Purpose : Tutorials and demonstration for basics of python programming
Pre-requisites : Python3 installation.
"""

#basics of python

#variables and data-types

#numeric datatypes with examples
integer_variable = 123
complex_variable = 123j
float_variable = 123.22

#sequence type
string_variable = "i am a string"
tuple_variable = ("android","apple","blackberry","windows") #immutable 
list_variable = ["android","apple","blackberry","windows"] #mutable 

#other types
boolean_variable = True
boolean_variable = False
dictionary_variable = {"l_number": 179144 , "name":"raghul gopalakrishnan", "course" : "MSc in computing in cloud technologies"}
set_variable = {"android","windows","apple","blackberry"} #unordered, mutable 
frozenset_variable = frozenset({"android","windows","apple","blackberry"})  #unordered, immutable 
none_variable = None #null or no value

print()
print("variables, data-types and Assignments")
print("======================================")
print("{0} is a {1}".format(integer_variable,type(integer_variable)))
print("{0} is a {1}".format(complex_variable,type(complex_variable)))
print("{0} is a {1}".format(float_variable,type(float_variable)))
print("{0} is a {1}".format(string_variable,type(string_variable)))
print("{0} is a {1}".format(tuple_variable,type(tuple_variable)))
print("{0} is a {1}".format(list_variable,type(list_variable)))
print("{0} is a {1}".format(boolean_variable,type(boolean_variable)))
print("{0} is a {1}".format(dictionary_variable,type(dictionary_variable)))
print("{0} is a {1}".format(set_variable,type(set_variable)))
print("{0} is a {1}".format(frozenset_variable,type(frozenset_variable)))
print("{0} is a {1}".format(none_variable,type(none_variable)))

#Assignments

integer_variable = 4
string_variable = "any string"

#Arithmetic Operators

integer_variable_1 = 2
integer_variable_2 = 4

addition = integer_variable_1 + integer_variable_2
subtraction = integer_variable_1 - integer_variable_2
division = integer_variable_1 / integer_variable_2
multiplication = integer_variable_1 * integer_variable_2
exponentiation = integer_variable_1 ** integer_variable_2
modulus = integer_variable_1 % integer_variable_2
floor_division = integer_variable_1 // integer_variable_2

print()
print("arithmetic operators")
print("=====================")
print("addition of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,addition))
print("subtraction of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,subtraction))
print("division of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,division))
print("multiplication of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,multiplication))
print("exponentiation of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,exponentiation))
print("modulus of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,modulus))
print("floor_division of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,floor_division))

#Comparison Operators
print()
print("comparison operators")
print("====================")
print("comparing equals of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,integer_variable_2 == integer_variable_1))
print("comparing not equals of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,integer_variable_2 != integer_variable_1))
print("comparing greater than of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,integer_variable_2 > integer_variable_1))
print("comparing lesser than or equals of {0} and {1} is {2}".format(integer_variable_1,integer_variable_2,integer_variable_2 <= integer_variable_1))

#Budget exercise
print()
print("budget exercise : ")
print("==================")

course_fees = 12000
loan_total_amount = 20000
rent_per_month = 400
expenses_per_month = 200
bills_per_month = 100
money_reserved_after_fee = loan_total_amount - course_fees
total_expenses_per_month =  (rent_per_month+expenses_per_month+bills_per_month)
money_after_first_month = money_reserved_after_fee - total_expenses_per_month
predicted_total_money_spent = course_fees + (total_expenses_per_month*12)

print("total fee : {}".format(course_fees))
print("loan amount : {}".format(loan_total_amount))
print("rent per month : {}".format(rent_per_month))
print("expenses per month : {}".format(expenses_per_month))
print("bills per month : {}".format(bills_per_month))
print("money remainang after fee : {}".format(money_reserved_after_fee))
print("total expenses per month : {}".format(total_expenses_per_month))
print("Prediction of total money needed for the year, including course fee : {}".format(predicted_total_money_spent))


#string exercises
print()
print("Playing with String")
print("====================")

string_variable = "this is a sample string."
print(f"to print first 4 letters of : {string_variable}, using slicing, result is : {string_variable[0:4:1]}")
print(f"trying to make {string_variable}, as uppercase with .upper function, the result is : {string_variable.upper()}")
print(f"trying to find length of : {string_variable},  with len function, the result is : {len(string_variable)}")




