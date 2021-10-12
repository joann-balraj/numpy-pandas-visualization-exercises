import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?
negative = [num for num in a if num < 0]
print(len(negative))

# 2. How many positive numbers are there?
positive = a[a > 0]
#positive = [num for num in a if num > 0]
print(len(positive))

# 3. How many even positive numbers are there?
positive_even = [num for num in a if num > 0 and num % 2 == 0]
print(len(positive_even))

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
plus_three = [num + 3 for num in a]
plus_three_pos_count = [num for num in plus_three if num > 0]
print(len(plus_three_pos_count))

# 5. If you squared each number, what would the new mean and standard deviation be?
squared = [num ** 2 for num in a]
squared_array = np.array(squared)
mean = squared_array.mean()
std = squared_array.std()
print(mean)
print(std)

# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.
mean_a = [num.mean() for num in a]
print(mean_a)
mean_a = np.array(mean_a)
print(mean_a.mean())

# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
