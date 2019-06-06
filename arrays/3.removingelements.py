from array import *

arr1 = array('i', [1,2,3,4,5,6,7,8,9])
print('Initial Array: ', arr1)
arr1.remove(2)
print('Removing ''2'' from the array: ', arr1)
arr1.pop()
print('Removing last element: ', arr1)
print(arr1.index(3))
arr1.reverse()
print('Reversed Array: ', arr1)
