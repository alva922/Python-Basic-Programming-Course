#https://newdigitals.org/2024/01/23/basic-python-programming/#conditionals
# Conditionals
# Python Conditions and If statements support the usual logical conditions
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")
Output:
b is greater than a

#The elif keyword is Python’s way of saying “if the previous conditions were not true, then try this condition”
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
Output:
a and b are equal

#The else keyword catches anything which isn’t caught by the preceding conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
Output:
a is greater than b

#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
Output:
Both conditions are True

#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
Output:
At least one of the conditions is True

#Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
Output:
a is NOT greater than b
#You can have if statements inside if statements, this is called nested if statements
x = 41
 
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
Output:
Above ten,
and also above 20!


