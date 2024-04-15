# https://newdigitals.org/2024/01/23/basic-python-programming/#loops
# Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). Loop through the letters in the word “banana”:
for x in "banana":
  print(x)
Output:
b
a
n
a
n
a
#With the break statement we can stop the loop before it has looped through all the items:
#Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
 
Output:
apple
banana

#To loop through a set of code a specified number of times, we can use the range() function

for x in range(6):
  print(x)
 
Output:
0
1
2
3
4
5
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter:
for x in range(2, 30, 3):
  print(x)
Output:
2
5
8
11
14
17
20
23
26
29

#A nested loop is a loop inside a loop. The “inner loop” will be executed one time for each iteration of the “outer loop”:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
 
for x in adj:
  for y in fruits:
    print(x, y)
Output:
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry

#With the while loop we can execute a set of statements as long as a condition is true. Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
Output:
1
2
3
4
5
