from array import *
arr1 = array('i', [1,2,3,4,5,6,7,8,9])
print('Initial Array: ', arr1)
arr1.insert(0,23)
print('adding 23 to the start of the array: ', arr1)
arr1.append(50)
arr2 = array('i', [10, 20, 30])
arr1.extend(arr2)

print('Extended array: ', arr1)

list1 = [100,200,300]
arr1.fromlist(list1)
print('addling list to the array:', arr1)
