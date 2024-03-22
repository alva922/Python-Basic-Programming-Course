#https://newdigitals.org/2024/01/23/basic-python-programming/#using-strings
#Assigning a single-line string to a variable
a = "Hi!"
print(a)
#Hi!
#Assigning a multi-line string to a variable
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.
#Loop through the letters in the word “banana”:
for x in "banana":
  print(x)
#b
#a
#n
#a
#n
#a
#The len() function returns the length of a string
a = "Hello, World!"
print(len(a))
#13
#To check if a certain phrase or character is present in a string, we can use the keyword in:
txt = "The best things in life are free!"
print("free" in txt)
#True
#Check if “expensive” is NOT present in the following text
txt = "The best things in life are free!"
print("expensive" not in txt)
#True
#You can return a range of characters by using the slice syntax
b = "Hello, World!"
print(b[2:5])
#llo
#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
#Hello
#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
#llo, World!
#Use negative indexes to start the slice from the end of the string:
#From: "o" in "World!" (position -5) 
#To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
#orl
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#HELLO, WORLD!
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#hello, world!
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#Hello, World!
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#Jello, World!
#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#['Hello', ' World!']
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
#HelloWorld
#To add a space between them, add a ” “:
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Hello World
