import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a/10
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
def product_of_a_function(a):
    result = 1
    for x in a:
         result = result * x
    return result
product_of_a = product_of_a_function(a)
print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [num ** 2 for num in a]
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [num for num in a if num % 2 != 0]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [num for num in a if num % 2 == 0]
print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)
sum_of_b = [sum(row) for row in b]
print(sum_of_b)
# Exercise 2 - refactor the following to use numpy.   
min_of_b = [min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])]
print(min_of_b)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = [max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])]
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = [(sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))]
print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = np.prod(b)
print(product_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = np.square(b)
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = [number for row in b for number in row if number % 2 != 0]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = [number for row in b for number in row if number % 2 == 0]
print(evens_in_b)

# Exercise 9 - print out the shape of the array b.
print(np.shape(b))

# Exercise 10 - transpose the array b.
print(np.transpose(b))

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(np.reshape(b, (1, 6)))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(np.reshape(b, (6, 1)))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)

# Exercise 1 - Find the min, max, sum, and product of c.
min = np.min(c)
max = np.max(c)
sum = np.sum(c)
product = np.product(c)
print('min: ', min, ' max: ', max, ' sum: ', sum, ' product: ', product)

# Exercise 2 - Determine the standard deviation of c.
std = np.std(c)
print(std)

# Exercise 3 - Determine the variance of c.
## The variance is the average of the squared deviations from the mean, i.e., var = mean(x), where x = abs(a - a.mean())**2.
variance = np.var(c)
print(variance)

# Exercise 4 - Print out the shape of the array c
shape = np.shape(c)
print(shape)

# Exercise 5 - Transpose c and print out transposed result.
trans_c = np.transpose(c)
print(trans_c)

# Exercise 6 - Get the dot product of the array c with c. 
prod_of_c_and_c = np.dot(c, c)
print(prod_of_c_and_c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sum_of_c_and_c_transposed = c * trans_c
print(np.sum(sum_of_c_and_c_transposed))

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
product_of_c_and_c_transposed = c * trans_c
print(np.product(sum_of_c_and_c_transposed))

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
sine_d = np.sin(d)
print(sine_d)

# Exercise 2 - Find the cosine of all the numbers in d
cosine_d = np.cos(d)
print(cosine_d)

# Exercise 3 - Find the tangent of all the numbers in d
tangent_d = np.tan(d)
print(tangent_d)

# Exercise 4 - Find all the negative numbers in d
neg_d = d[d < 0]
print((neg_d))

# Exercise 5 - Find all the positive numbers in d
pos_d = d[d > 0]
print((pos_d))

# Exercise 6 - Return an array of only the unique numbers in d.
unique = np.unique(d)
print(unique)

# Exercise 7 - Determine how many unique numbers there are in d.
print(len(unique))

# Exercise 8 - Print out the shape of d.
print(np.shape(d))

# Exercise 9 - Transpose and then print out the shape of d.
d = np.transpose(d)
print(np.shape(d))

# Exercise 10 - Reshape d into an array of 9 x 2
d_9_x_2 = np.reshape(d, (9, 2))
print(d_9_x_2)