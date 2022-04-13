# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product
# of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

num_list = [3, 2, 1]
num_list2 = [1, 2, 3, 4, 5]
product_list = []

# With division
for i in num_list2:
    product = 1
    for j in num_list2:
        product *= j
    product //= i
    product_list.append(product)

print(product_list)

product_list = []

# Without division
for index_i, i in enumerate(num_list2):
    product = 1
    for index_j, j in enumerate(num_list2):
        if index_i == index_j:
            continue
        product *= j
    product_list.append(product)

print(product_list)