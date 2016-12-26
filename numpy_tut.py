import numpy as np

a = np.zeros((3,4)) #create a 3x4 array of zeroes
b = np.array([(1,2),(3,4)]) #create a 2x2 array, (1,2) and (3,4) are rows
c = np.arange(2) #create a 2 element column vector with elements 1 ... 2
d = np.arange(12).reshape(4,3) #create a 4x3 array with elements 1 ... 12. The numbers are filled row by row
e = np.random.random((2,3)) #create a 2x3 array with random elements between 0 and 1
f = np.sin(b) #create a new matrix whose elemnts are the sin of those of b

g = np.append(b, [[5,6]], axis = 0) #add a row to matrix b

print(b[0]) #print the first row of b
print(b[:,0]) #print the first column of b
print(b[0,1]) #print the element in the first row and second column of b
print(np.dot(b,c)) #multiply "arrays" b and c
print(np.transpose(b)) #print the transpose of "array" b
print(np.mean(b)) #print the mean of all elements in b
print(np.mean(b, axis = 0)) #print the mean of each column
print(np.mean(b, axis = 1)) #print the mean of each row
print(np.std(b)) #print the standard deviation of elements in b (you can specify the axis)



#Note: You could use np.matrix instead of np.array (with some slight parameter modifications)
#The reason I don't here is because arrays are more general and versatile, and still encompass all the functionality of a numpy matrix
