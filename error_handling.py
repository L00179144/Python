"""
Author : Raghul Gopalakrishnan
Contact : raghulgk@gmail.com
Purpose : Tutorials and demonstration for functions in python programming
Pre-requisites : Python3 installation.
"""

my_filename = "logfile.txt"

try:
    with open(my_filename, "a") as file_handle:
        print(f"Writing a test line to {my_filename}")
        file_handle.write("Test line")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
else:
    print("File created")
finally:
    print("Finishing up!")
    # close not needed because with statement
    # file_handle.close()



def validate_integer():
    # Loop forever
    while True:
        try:
            fuel_quantity = int(input("Enter how much fuel you have in vehicle: "))
            fuel_consumption = int(input("Enter how much mielage per litre: "))
            endurance = fuel_quantity/fuel_consumption
            print(f"endurance = {endurance}")
        except:
            # Bad value, 
            print("Error")
            raise Exception("Values must be an integer")
            continue
        else:
            print("Valid input")
            # Good value, exit the loop
            break
        finally:
            # Continue
            print("This message shows every time, regardless of the programme flow")
    

validate_integer()