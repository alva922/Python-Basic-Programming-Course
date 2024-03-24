#Boolean Values & Operators
#https://newdigitals.org/2024/01/23/basic-python-programming/#boolean-values-operators
#The Python Boolean type is one of Python’s built-in data types. It’s used to represent the truth value of an expression. Booleans represent one of two values: True or False:
#Input: 1==1
#Output: True 

#Input: 2<1 
#Output: False

#The output <class ‘bool’> indicates the variable is a Boolean data type

a = True
type(a)
 
b = False
type(b)
 
Output:
 
<class 'bool'>
<class 'bool'>

#When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)
Output:
True
False
False
#Print a message based on whether the condition is True or False:
a = 200
b = 33
 
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
Output:
b is not greater than a

#The bool() function allows you to evaluate any value, and give you True or False in return

print(bool("Hello"))
print(bool(15))
Output:
True
True

Boolean Operations in Python are simple arithmetic of True and False values:
#or
#and
#not
#== (equivalent)
#!= (not equivalent)

#Let’s try a Python Boolean with an if statement and OR operator that checks if a is greater than b or b is smaller than c and it returns 
#True if any of the conditions are True (b<c)
# Python program to demonstrate
# or operator
 
a = 1
b = 2
c = 4
 
if a > b or b < c:
    print(True)
else:
    print(False)
 
if a or b or c:
    print("At least one number has Boolean value as True")
Output:
True
At least one number has Boolean value as True
#Boolean And Operator: In the first part of the code,  the overall expression a > b and b < c evaluates to False. 
#Hence, the code will execute the else block and print False. Whereas in the second part, a is 0, conditions a and b, and c will evaluate to False 
#because one of the variables (a) has a Boolean value of False. 
# Python program to demonstrate
# and operator
 
a = 0
b = 2
c = 4
 
if a > b and b<c:
    print(True)
else:
    print(False)
     
if a and b and c:
    print("All the numbers has Boolean value as True")
else:
    print("At least one number has Boolean value as False")
Output:
False
At least one number has Boolean value as False

#The Boolean Not operator only requires one argument and returns the negation of the argument i.e. returns the True for False and False for True:
# Python program to demonstrate
# not operator
 
a = 0
 
if not a:
    print("Boolean value of a is False")
Output:
Boolean value of a is False

#Boolean == (equivalent) and != (not equivalent) Operator. Both operators are used to compare two results. =
#= (equivalent operator returns True if two results are equal and != (not equivalent operator returns True if the two results are not same.

# Python program to demonstrate
# equivalent an not equivalent
# operator
 
a = 0
b = 1
 
if a == 0:
    print(True)
     
if a == b:
    print(True)
     
if a != b:
    print(True)
Output:
True
True

#The is keyword is used to test whether two variables belong to the same object. The test will return True if the two objects are the same else it will return False even if the two objects are 100% equal. The code below first assigns the value 10 to variables x and y. It then compares x and y using the “is” operator and prints True because they refer to the same object. 
#Next, it assigns two separate lists to x and y. 
#It then compares x and y using the “is” operator and prints False because the lists are different objects in memory. 
#Therefore, the code will execute the else block and print “At least one number has a Boolean value as False”.

# Python program to demonstrate
# is keyword
  
  
x = 10
y = 10
  
if x is y:
    print(True)
else:
    print(False)
  
x = ["a", "b", "c", "d"]
y = ["a", "b", "c", "d"]
  
print(x is y)
Output:
True
False
#in operator checks for the membership i.e. checks if the value is present in a list, tuple, range, string, etc. 
#The code below creates a list of animals and checks if the string “lion” is present in the list. 
#If “lion” is found in the list, it prints “True”.
# Python program to demonstrate
# in keyword
  
# Create a list
animals = ["dog", "lion", "cat"]
  
# Check if lion in list or not
if "lion" in animals:
    print(True)
Output:
True
#Python also has many built-in functions that return a Boolean value, 
#like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
Output:
True

