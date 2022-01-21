from numpy import*
arr1 = array([10,22,13,41,])
arr2 = array([12,23,24,25])

arr3 = arr1 + arr2
print(arr3)
print(sort(arr1))
print(max(arr2))

#copy array but memory location of both the array is same
arr4 = arr1
print(arr4)
#beow print will print the address of memory location for both the arrays
print(id(arr1))
print(id(arr4))

# below view function to copy array including values in array but at different memory location
# view function will give you shallow copy that means there will be dependency of arrays on each other
#so when you change value in one array, it will change in another array as well
arr5 = arr1.view()
print(id(arr1))
print(id(arr5))

# copy function will give you deep copy, no dependency of arrays
arr6 = arr1.copy()
arr1[1] = 3445
print(id(arr6))
print(arr6)