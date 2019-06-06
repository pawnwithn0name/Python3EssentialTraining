# importing an array 

# from array import *

# declaring an array

# arrayIdentifierName  =  array[typecode,  (Initialiers)]

# Program 1 - creating and printing an array
'''
from array import *

my_array = array('i', [76, 4559, 2100, 235])

print("Array is: ")
for i in my_array:
	print( i, end = ' ' )
print()
'''

# Program 2 - Accessing Elements of an array

from array import *

my_array = array('i', [76, 4559, 2100, 235, 450, 567, 98])

print("Array is: ")
for i in my_array:
	print( i, end = ' ' )
print()
print("Second Element: ", my_array[1])
print()
print("Sum of first and last element: ", my_array[0] + my_array[len(my_array) - 1])
print()
