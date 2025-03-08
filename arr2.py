import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])


arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr1[0:2, 1:4])
arr3 = np.array([1,2,3])
astype() #function



arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)