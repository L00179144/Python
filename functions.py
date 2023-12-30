"""
Author : Raghul Gopalakrishnan
Contact : raghulgk@gmail.com
Purpose : Tutorials and demonstration for functions in python programming
Pre-requisites : Python3 installation.
"""

#functions
def sample_functions():
    print("this is a sample function")

sample_functions()

#function with parameter
def sample_function_with_parameters(y):
    z = 100
    x = y + z
    print(f"addition of {z} and {y} is {x}")

sample_function_with_parameters(50)

#function with number of parameters
def sample_function_with_n_parameters(*parameters):
    total = 0
    for number in parameters:
        total = total + number
    print(f"addition all numbers in {parameters} is {total}")

sample_function_with_n_parameters(1,2,3,4,5,6)

#function with return 
def area_of_rectangle(length, breath) :
    area = length * breath
    return area

print(f"area of rectangle is {area_of_rectangle(10,20)}") 


#lambda 
def area_of_rectangle_lambda(length:int, breath:int) -> int :
    return length * breath

print(f"area of rectangle in lambda is {area_of_rectangle_lambda(10,20)}") 


#lambda 
def area_of_cylinder_lambda(radius:int, height:int) -> float :
    return 3.14 * radius * radius * height

print(f"area of cylinder in lambda is {area_of_cylinder_lambda(10,20)}") 


def true_if_even(array) -> bool:
    result = False
    for items in array :
        if(items % 2 == 0):
            result = True
    return result

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(f"Is there a even number in {array} : {true_if_even(array)}")