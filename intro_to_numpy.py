import numpy as np

# Basics
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(arr1.dtype) #int32 
print(arr1.size)
print(np.array([1,2,3,4,5],dtype=np.float64))

for item in arr1: # can loop through just like normal
    print(item, end=' ')

#2D arrays; shape, dimensions
arr2 = np.array([[1,2],[3,4],[5,6]])
print(arr2)
print(arr1.shape)
print(arr2.shape)

print(arr1.ndim)
print(arr2.ndim)

print(arr2.reshape(6,))
print(arr2.reshape(2,3))
print(arr2.reshape(2,3,1))

# Special arrays
print(np.ones(10))
print(np.ones(shape=(5,2)))
print(np.zeros(10))
print(np.empty(10))
print(np.arange(50))
print(np.linspace(10,20,5))

print(np.max(arr2))
print(np.min(arr2))
print(np.sum(arr2))

# Array arithmetic
arr3 = np.arange(10,20)
print(arr3)
arr3_modified = arr3*2
print(arr3_modified)
print(arr3 + arr3_modified)

# Array indexing & slices
print(arr3[5:7])

arr4 = arr3.reshape(5,2)
print(arr4)
print(arr4[3:4,:1])
print(arr4[3:4,:])

# Conditional slicing 
print(arr3[arr3 > 15])
print(arr3[arr3 < 17])
print(arr3[(arr3 > 15) & (arr3 < 17)])
print(arr3[(arr3 > 15) | (arr3 < 17)])