"""
Author : Raghul Gopalakrishnan
Contact : raghulgk@gmail.com
Purpose : Tutorials and demonstration for object oriented coding in python programming
Pre-requisites : Python3 installation.
"""


#class and object

class Employee:
    # class variables
    company_name = 'Accenture Company'

    # constructor to initialize the object
    def __init__(self, name, salary):
        # instance variables
        self.name = name
        self.salary = salary

    # instance method
    def show(self):
        print('Employee:', self.name, self.salary, self.company_name)

# create first object
emp1 = Employee("Raghul", 32000)
emp1.show()

# create second object
emp2 = Employee("Shahanawaz", 41000)
emp2.show()

# Method Overloading

class employee1():
    def name(self):
        print("Harshit is his name")    
    
    def salary(self):
        print("3000 is his salary")
 
    def age(self):
        print("22 is his age")
 
class employee2():
    def name(self):
        print("Rahul is his name")
 
    def salary(self):
        print("4000 is his salary")
 
    def age(self):
        print("23 is his age")
 
def func(obj):
    obj.name()
    obj.salary()
    obj.age()
 
obj_emp1 = employee1()
obj_emp2 = employee2()
 
func(obj_emp1)
func(obj_emp2)


#Inheritance

# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee1(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee1()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')
