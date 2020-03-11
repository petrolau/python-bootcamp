#importing the module
import numpy as np

my_list = [1,2,3]
#numpy array
arr = np.array(my_list)
print(arr)

#displaying matrix 
my_mat = [[1,2,3],[4,5,6],[7,8,9]]

print(np.array(my_mat))

#np.arange -> similar to python`s range function
#generating arrays jumping 2 from 2
print(np.arange(0,10,2))

#generating a array full of zeros
#((row,column))
print(np.zeros((3,4)))

print(np.ones((3,4)))

#linspace -> evenly spaced numbers from 0 to 5
print(np.linspace(0,5,10))

#identity matrix using numpy
print(np.eye(4))

#np random.rand() --> populating the list with random numbers 0-1
print(np.random.rand(5,5))

#np ramdom.randn()
print(np.random.randn(2))

#np random.randint()
print(np.random.randint(1,100))

#reshape method --> total size of the new array must be unchanged
arr2 = np.arange(25)
print(arr2.reshape(5,5))

#max method -> max value of that array
print(arr2.max())

#knowing at which index value my lowest of highest value is .
print(arr2.argmax())
print(arr2.argmin())

#figure the shape of the vector
arr3=arr2.reshape(5,5)
print(arr3.shape)

#
