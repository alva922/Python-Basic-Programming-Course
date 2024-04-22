#https://newdigitals.org/2024/01/23/basic-python-programming/#functions
#Functions
'''
Python Function is a block of statements that return the specific task. 
The idea is to put some commonly or repeatedly done tasks together and make a function so that instead 
of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
There are mainly two types of functions in Python.
Built-in library function: These are Standard functions in Python that are available to use.
User-defined function: We can create our own functions based on our requirements.
We can define a function using the def keyword
'''
# A simple Python function
def fun():
    print("Welcome to Python")
 
 
# Driver code to call a function
fun()
Output:
Welcome to Python
'''
You can pass data, known as parameters, into a function.
A function can return data as a result.
Information can be passed into functions as arguments. 
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma:
'''
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
 
    return num3
 
# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
Output:
The addition of 5 and 15 results 20.
# some more functions
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))
 
Output:
False True

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
  print("The youngest child is " + kids[2])
 
my_function("Emil", "Tobias", "Linus")
Output:
The youngest child is Linus

#Keyword Arguments: You can also send arguments with the key = value syntax

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
 
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
The youngest child is Linus

#If you do not know how many keyword arguments that will be passed into your function, 
#add two asterisk: ** before the parameter name in the function definition.
def my_function(**kid):
  print("His last name is " + kid["lname"])
 
my_function(fname = "Tobias", lname = "Refsnes")
Output:
His last name is Refsnes
'''
You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function. 
E.g. if you send a List as an argument, it will still be a List when it reaches the function:
'''
def my_function(food):
  for x in food:
    print(x)
 
fruits = ["apple", "banana", "cherry"]
 
my_function(fruits)
 
Output:
apple
banana
cherry

#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x
 
print(my_function(3))
print(my_function(5))
print(my_function(9))
Output:
15
25
45

#A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))
Output:
15

#Lambda functions can take any number of arguments:

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))
Output:
30
