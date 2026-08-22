# Indexing 
import numpy as np
one_d = np.array([1,2,3,4,5,6])
print(one_d)
print(one_d[0]) # first element


two_d =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d)
print(two_d[1,2]) # second row, third column

print(two_d[0:2,1:3]) # first two rows, second and third columns

print(two_d[1,1]) # second row, second column
print(two_d[1][1]) # second row, second column
print(two_d[2,0]) # third row, first column (this will raise an IndexError since the index is out of bounds)


three_d = np.array([[[1,2,3,4],[4,5,6,7]],[[1,2,3,4],[4,5,6,7]]])
print(three_d)

#[a,b,c] -> a = 2d array, b = 1d array, c = 0d array

print(three_d[1,0,3]) # second 2d array, first 1d array, fourth element
print(three_d[1,1,1]) # second 2d array, second 1d array, second element


# Slicing -->

one_d = np.array([1,2,3,4,5,6])
print(one_d) 
print(one_d[1:4]) # second to fourth elements

two_d = np.array([[1,2,3,5],[4,5,6,7],[4,5,6,7]])
print(two_d)
print(two_d[0,1:3]) # first row, second and third columns
print(two_d[0:2,1:4]) # first two rows, second to fourth columns



three_d =np.array([[[1,2,3,5],[4,5,6,7]],[[1,2,3,4],[10,20,30,40]]])
print(three_d)
print(three_d[0,0:2,1:3]) # first 2d array, first 1d array, second and third elements

print(three_d[0:2,0:2,1:3]) # first two 2d arrays, first 1d array, second and third elements


# Reshape -->


# it is just used to change the shape of array(changing the dimensions of array) without changing the data of array
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)

arr4 = arr.reshape(3,3) # reshape to 3x3 array
print(arr4)


print(arr.ndim)

print(arr.shape)

arr = np.array([1,2,3,4,5,6,7,8])
arr1 = arr.reshape(2,4)
print(arr1)


arr1 = arr.reshape(4,2)
print(arr1)

arr = np.array([[1,23,4],[4,5,6],[7,8,9]])
print(arr)

arr1 = arr.reshape(9,1)
print(arr1)


arr = np.array([1,2,3,4,5,6,7,8])
print(arr)

#MNIST dataset

# Converting this one-d array into 3 - d

arr2 = arr.reshape(2,2,2) # 2*2*2
print()


#converting this one-d array into 3 -d 
arr2 = arr.reshape(4,2,1)
print(arr2)


#Converting this one-d array into 3 -d 
arr2 = arr.reshape(2,1,4)
print(arr2)


# 2-d to 1-d

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)


arr1 = arr.reshape(9,)
print(arr1)


# arr.reshape(2,2,-1)   -> 2*2*? = 8



# Methods to create numpy array

# zero()
#ones()
#arrange()
#identity()
#eye()


#np.zero() -> it is used to create an array full of 0

arr = np.zeros(6,dtype=int)
print(arr)

# np.zeros() - > it is used to create an full of 0
arr = np.zeros((4,3),dtype = int)
print(arr)

#np.ones() - > used to create an array full of 1
 
arr = np.ones((4,3),dtype=int)
print(arr)

#np.full() -> shape, values, fill the entire array with value

arr = np.full((4,3),100)
print(arr)

#create an array in the given range

arr = np.arange(10)
print(arr)

arr = np.arange(2,11,3)
print(arr)

for i in range(2,11,3):
  print(i,end =" ")

# identity() - > creates a identity matrix

arr = np.identity(5,dtype = int)
print(arr)

#np.identity => rows == column
#np.eye => rows != column
arr = np.eye(4,3,dtype = int)
print(arr)


#Random Module

#np.random.randint()
#randint() => random + int
x = np.random.randint(1,100)
print(x)

x = np.random.randint(1,100, size = 20)


#choice

dice = [1,2,3,4,5,6]
roll = np.random.choice(dice)
print(roll)



# Arithmetic operations in Numpy

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
print(l1+l2)


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 + arr2)


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 - arr2)


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 / arr2)


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 * arr2)


# Mean -> Average-> Sum of all the elements / number of element 
arr = np.array([10,20,21,25,35,45])
print(arr)


# median -> middle value
# median -> odd length -> 1 median
# even length -> 2 median => average of 2 median
arr = np.array([10,20,21,25,35,45,50])
ans = np.median(arr)
print(ans)



# sort 
arr = np.array([11,1,15,4,21,13])
arr_sorted = np.sort(arr)
print(arr_sorted)

#descending order
arr = np.array([11,1,15,4,21,13])
arr_sorted = np.sort(arr)[::-1]
print(arr_sorted)



import numpy as np

arr = np.array([10, 50, 5, 80, 25])

# Method 1: Negate the array before argsort
desc_idx = (-arr).argsort()
sorted_desc = arr[desc_idx]

print("Descending indices:", desc_idx)
print("Sorted descending:", sorted_desc)



























