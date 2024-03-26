#https://newdigitals.org/2024/01/23/basic-python-programming/#lists
#Lists are used to store multiple items in a single variable
mylist = ["apple", "banana", "cherry"]
print(mylist)
Output:
['apple', 'banana', 'cherry']
#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]
#Lists are defined as objects with the data type ‘list’
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
Output:
<class 'list'>
#It is also possible to use the list() constructor when creating a new list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
Output:
['apple', 'banana', 'cherry']
#To determine how many items a list has, use the len() function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
Output:
3
#In order to access the list items refer to the index number. Use the index operator [ ] to access an item in a list
# Python program to demonstrate
# accessing of element from list
  
# Creating a List with
# the use of multiple values
List = ["Go", "For", "Python"]
  
# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])
 
Output:
Accessing a element from the list
Go
Python
#Accessing elements from a multi-dimensional list
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Go', 'For'], ['Python']]
  
# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
Output:
Accessing a element from a Multi-Dimensional list
For
Python
#Negative Indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.
#(the first item has index 0)
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
Output:
cherry
#You can specify a range of indexes by specifying where to start and where to end the range, e.g. return the third, fourth, and fifth item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
Output:
['cherry', 'orange', 'kiwi']
#This example returns the items from the beginning to, but NOT including, “kiwi”
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
Output:
['apple', 'banana', 'cherry', 'orange']
#This example returns the items from “orange” (-4) to, but NOT including “mango” (-1)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
Output: 
['orange', 'kiwi', 'melon']
#To determine if a specified item is present in a list use the in keyword
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
Output:
Yes, 'apple' is in the fruits list
To change the value of a specific item, refer to the index number
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
Output:
['apple', 'blackcurrant', 'cherry']
#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
Output:
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
Output:
['apple', 'blackcurrant', 'watermelon', 'cherry']
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly, 
#e.g. change the second and third value by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
Output:
['apple', 'watermelon']
#To insert a new list item, without replacing any of the existing values, we can use the insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
Output:
['apple', 'banana', 'watermelon', 'cherry']
#To add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
Output:
['apple', 'banana', 'cherry', 'orange']
#To append elements from another list to the current list, use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
Output:
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
#The remove() method removes the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
Output:
['apple', 'cherry']
#The pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
Output:
['apple', 'cherry']
#The del keyword can also delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist
#The clear() method empties the list. The list still remains, but it has no content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
Output:
[]
#You can loop through the list items by using a for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
Output:
apple
banana
cherry
