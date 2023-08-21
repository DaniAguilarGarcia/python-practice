'''Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] 
to numpy arrays arr1 and arr2. 
Then find the even and odd numbers from arr1 and arr2'''

import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])


#Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:1]
print("even for array1", even_arr1)

#Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1 = arr1[0:5:2]
print("odd for array1",odd_arr1)

#Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2", even_arr2)

#Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2=arr2[1:5:2]
print("odd for array2",odd_arr2)