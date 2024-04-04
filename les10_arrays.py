#https://newdigitals.org/2024/01/23/basic-python-programming/#arrays
#An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. 
#The array can be handled in Python by a module named array. 
#A user can treat lists as arrays. However, the user cannot constrain the type of elements stored in a list. If you create arrays using the array module, all elements of the array must be of the same type. 
#This code below creates two arrays: one of integers and one of doubles. It then prints the contents of each array to the console:
import array as arr
a = arr.array('i', [1, 2, 3])
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("\nThe new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
Output:
The new created array is :  1 2 3
 
The new created array is :  2.5 3.2 3.3
#Elements can be added to the Array by using built-in insert() function. Insert is used to insert one or more data elements into an array. Based on the requirement, a new element can be added at the beginning, end, or any given index of array. append() is also used to add the value mentioned in its arguments at the end of the array. 
import array as arr
a = arr.array('i', [1, 2, 3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
a.insert(1, 4)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()
b.append(4.4)
print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print()
Output:
Array before insertion :  1 2 3
Array after insertion :  1 4 2 3
Array before insertion :  2.5 3.2 3.3
Array after insertion :  2.5 3.2 3.3 4.4

#In order to access the array items refer to the index number. Use the index operator [ ] to access an item in a array. The index must be an integer. 
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[0])
print("Access element is: ", a[3])
b = arr.array('d', [2.5, 3.2, 3.3])
print("Access element is: ", b[1])
print("Access element is: ", b[2])
Output:
Access element is:  1
Access element is:  4
Access element is:  3.2
Access element is:  3.3
#Elements can be removed from the array by using built-in remove() function but an Error arises if element doesn’t exist in the set.
#In Python array, there are multiple ways to print the whole array with all the elements, but to print a specific range of elements from the array, we use Slice operation. Slice operation is performed on array with the use of colon(:). To print elements from beginning to a range use [:Index], to print elements from end use [:-Index], to print elements from specific Index till the end use [Index:], to print elements within a range, use [Start Index:End Index] and to print whole List with the use of slicing operation, use [:]. Further, to print whole array in reverse order, use [::-1].
import array as arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)
Sliced_array = a[5:]
print("\nElements sliced from 5th "
    "element till the end: ")
print(Sliced_array)
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)
 
Output:
 
Initial Array: 
1 2 3 4 5 6 7 8 9 10
Slicing elements in a range 3-8: 
array('i', [4, 5, 6, 7, 8])
 
Elements sliced from 5th element till the end: 
array('i', [6, 7, 8, 9, 10])
 
Printing all elements using slice operation: 
array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#read more
#https://www.geeksforgeeks.org/python-arrays/
