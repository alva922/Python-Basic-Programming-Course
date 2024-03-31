#https://newdigitals.org/2024/01/23/basic-python-programming/#sets
#In Python, a Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
#Set items are unchangeable, but you can remove items and add new items.
#The values True (False) and 1 (0) are considered the same value in sets, and are treated as duplicates.
#Set items can be of any data type.
#The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
#Sets are written with curly brackets:
thisset = {"apple", "banana", "cherry"}
print(thisset)
Output:
{'banana', 'cherry', 'apple'}
#To determine how many items a set has, use the len() function
thisset = {"apple", "banana", "cherry"}
 
print(len(thisset))
 
Output:
3
#Sets are defined as objects with the data type ‘set’:
myset = {"apple", "banana", "cherry"}
print(type(myset))
Output:
<class 'set'>
#It is possible to use the set() constructor to make a set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
Output:
{'banana', 'cherry', 'apple'}
#Creating a Set
# Python program to demonstrate 
# Creation of Set in Python
 
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
 
# Creating a Set with 
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)
 
# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)
 
# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)
 
# Creating a Set with
# the use of a tuple
t=("Geeks","for","Geeks")
print("\nSet with the use of Tuple: ")
print(set(t))
 
# Creating a Set with
# the use of a dictionary
d={"Geeks":1,"for":2,"Geeks":3}
print("\nSet with the use of Dictionary: ")
print(set(d))
 
Output:
Initial blank Set: 
set()
 
Set with the use of String: 
{'k', 'e', 'F', 'r', 'o', 'G', 's'}
 
Set with the use of an Object: 
{'k', 'e', 'F', 'r', 'o', 'G', 's'}
 
Set with the use of List: 
{'Geeks', 'For'}
 
Set with the use of Tuple: 
{'Geeks', 'for'}
 
Set with the use of Dictionary: 
{'Geeks', 'for'}
#Python has a set of built-in methods that you can use on sets: add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, isubset, etc.
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method
thisset = {"apple", "banana", "cherry"}
 
thisset.add("orange")
 
print(thisset)
Output:
{'orange', 'banana', 'cherry', 'apple'}
#To add items from another set into the current set, use the update() method, e.g. add elements from tropical into thisset
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
 
thisset.update(tropical)
 
print(thisset)
 
Output:
{'banana', 'cherry', 'mango', 'papaya', 'apple', 'pineapple'}
#To remove an item in a set, use the remove(), or the discard() method
thisset = {"apple", "banana", "cherry"}
 
thisset.remove("banana")
 
print(thisset)
 
Output:
{'cherry', 'apple'}
#Other options: the clear() method empties the set; the del keyword will delete the set completely
#Loop through the set, and print the values
thisset = {"apple", "banana", "cherry"}
 
for x in thisset:
  print(x)
banana
cherry
apple

#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
 
set3 = set1.union(set2)
print(set3)
Output:
{1, 2, 3, 'a', 'b', 'c'}
#The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
 
z = x.intersection(y)
 
print(z)
 
Output:
{'apple'}
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
 
x.symmetric_difference_update(y)
 
print(x)
Output:
{'banana', 'google', 'microsoft', 'cherry'}
