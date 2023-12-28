"""
Author : Raghul Gopalakrishnan
Contact : raghulgk@gmail.com
Purpose : Tutorials and demonstration for data-structures of python programming
Pre-requisites : Python3 installation.
"""

#datastructures

print("working with lists :")
print("======================")

list_variable = ["android","apple","blackberry","windows"] 

print(f"my list : {list_variable}")

#using len() function in list
length_of_list = len(list_variable)
print(f"length of my list using len() : {length_of_list}")

#concatinate list with another list 

list_variable_1 = ["linux","chromeOS"] 
print(f"my second list : {list_variable_1}")
concatinated_list = list_variable + list_variable_1
print(f"my concatinated list using + operator : {concatinated_list}")

list_of_list = [list_variable, list_variable_1]
print(f"list of list : {list_of_list}")

print() 

#tuple
print("working with tuple :")
print("=====================")
tuple_variable = ("android","apple","blackberry","windows","android")
#tuples are immutable, once created 
print(f"my tuple : {tuple_variable}")
print(f"length of my tuple : {len(tuple_variable)}")
tuple_index = tuple_variable.index("android")
tuple_count = tuple_variable.count("android")
print(f"index of android in my tuple : {tuple_index}")
print(f"count of android in my tuple : {tuple_count}")

print()

#dictionary
print("working with dictionary :")
print("=========================")

dictionary_variable = {
    "name" : "Raghul Gopalakrishnan",
    "date of birth" : "19 Dec 1992",
    "location" : "Ireland"
}
print(f"my dictionary : {dictionary_variable}")
dictionary_variable["Nationality"] = "Indian"
print(f"my dictionary after appending : {dictionary_variable}")

print(f"my dictionary items: {dictionary_variable.items()}")
print(f"my dictionary keys : {dictionary_variable.keys()}")
print(f"my dictionary values : {dictionary_variable.values()}")




