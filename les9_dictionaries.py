#https://newdigitals.org/2024/01/23/basic-python-programming/#dictionaries
#Dictionaries are used to store data values in key: value pairs.
#A dictionary is a collection which is ordered (as of Python version 3.7), changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
Output:
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#It is possible to use the dict() constructor to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
Output:
{'name': 'John', 'age': 36, 'country': 'Norway'}
#You can access the items of a dictionary by referring to its key name, inside square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print (x)
Output:
Mustang
#The keys() method will return a list of all the keys in the dictionary
x = thisdict.keys()
print (x)
Output:
dict_keys(['brand', 'model', 'year'])
#The values() method will return a list of all the values in the dictionary
x = thisdict.values()
print (x)
Output:
dict_values(['Ford', 'Mustang', 1964])
#Make a change in the original dictionary, and see that the values list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
 
x = car.values()
 
print(x) #before the change
 
car["year"] = 2020
 
print(x) #after the change
 
Output:
dict_values(['Ford', 'Mustang', 1964])
dict_values(['Ford', 'Mustang', 2020])
#Check if “model” is present in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
Output:
Yes, 'model' is one of the keys in the thisdict dictionary
#The update() method will update the dictionary with the items from the given argument
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print (thisdict)
Output:
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
#Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
Output:
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
Output:
{'brand': 'Ford', 'year': 1964}
#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
Output:
{}
#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
Output:
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#Add Items to a Python Dictionary with Different Data Types
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Go'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
 
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Python'}}
print("\nAdding a Nested Key: ")
print(Dict)
 
Output:
Empty Dictionary: 
{}
 
Dictionary after adding 3 elements: 
{0: 'Go', 2: 'For', 3: 1}
 
Dictionary after adding 3 elements: 
{0: 'Go', 2: 'For', 3: 1, 'Value_set': (2, 3, 4)}
 
Updated key value: 
{0: 'Go', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4)}
 
Adding a Nested Key: 
{0: 'Go', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4), 5: {'Nested': {'1': 'Life', '2': 'Python'}}}
#Dictionary Methods: clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, and values.
