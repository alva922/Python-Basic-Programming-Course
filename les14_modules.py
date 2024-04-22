#https://newdigitals.org/2024/01/23/basic-python-programming/#modules
#Modules
'''
Python Module is a file that contains built-in functions, classes and variables.
Consider a module to be the same as a code library. Let’s create a simple calc.py in which we define two functions, one add and another subtract.

'''
# A simple module, calc.py
def add(x, y):
    return (x+y)
 
def subtract(x, y):
    return (x-y)
'''
Save this code in a file named calc.py within the working directory.
Now, we are importing the calc that we created earlier to perform add operation.
'''
# importing module calc.py
import calc
 
print(calc.add(10, 2))
 
Output:
12

#The * symbol used with the import statement is used to import all the names from a module to a current namespace.
# importing sqrt() and factorial from the
# module math
from math import *
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))
Output:
4.0
720

#Directories List for Modules: sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search for the required module.

# importing sys module
import sys
  
# importing sys.path
print(sys.path)

#We can rename the module while importing it using the keyword.
# importing sqrt() and factorial from the
# module math
import math as mt
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(mt.sqrt(16))
print(mt.factorial(6))
Output:
4.0
720
#We can import specific names from a module without importing the module as a whole
# import only pi from math module
from math import pi
 
print(pi)
 
Output:
3.141592653589793

#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc.):
#Let’s the dictionary person1 in calc.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#Running the code snippet
import calc as mymod
 
a = mymod.person1["age"]
print(a)
 
Output:
36


