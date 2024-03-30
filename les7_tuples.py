#https://newdigitals.org/2024/01/23/basic-python-programming/#tuples
#Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable or immutable.
#It is an ordered collection, so it preserves the order of elements in which they were defined.
#Since tuples are indexed, they can have items with the same value (duplicates).
#Tuple items can be of any data type with strings, integers and Boolean values.
#Tuples are written with round brackets, separated by a comma:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
Output:
('apple', 'banana', 'cherry')

#As with Lists, you can use the len() function
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
Output:
3
#To create a tuple with only one item, you have to add a comma after the item
thistuple = ("apple",)
print(type(thistuple))
Output:
<class 'tuple'>
#It is also possible to use the tuple() constructor to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
Output: 
('apple', 'banana', 'cherry')
See below the Python programs to demonstrate the addition of elements in a Tuple:
# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)
  
# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)
  
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
  
# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)
 
Output:
Initial empty Tuple: 
()
 
Tuple with the use of String: 
('Geeks', 'For')
 
Tuple using List: 
(1, 2, 4, 5, 6)
 
Tuple with the use of function: 
('G', 'e', 'e', 'k', 's')

#Read more:

#Concatenation of Tuples
#Slicing of a Tuple is done to fetch a specific range or slice of sub-elements from a Tuple. Slicing can also be done to lists and arrays. 
#The entire tuple gets deleted by the use of del() method. 
#Built-In Methods (index, count) & Functions (all, any, len, enumerate, min, max, sum, sorted, tuple)

