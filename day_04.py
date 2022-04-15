# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

num_list = [2, 3, 7, 6, 8, -1, -10, 15]
num_list2 = [2, 3, -7, 6, 8, 1, -10, 15]
num_list3 = [-1, 0, 8, 1]

# first approach with splitting lists and validating a subset
def find_missing(num_list):
    if num_list[0] < 1:
        return 1
    elif num_list[0] != 1:
        return num_list[0] - 1
    for index in range(1, len(num_list) - 1):

        if num_list[index] != num_list[index - 1] + 1 and num_list[index] != 1:
            return num_list[index] - 1
        elif num_list[index] != num_list[index + 1] - 1:
            return num_list[index] + 1

# second approach, taking all values in the list into consideration
def sort_nums(num_list):
    min_positive_val = 1
    num_list.sort()
    for i in num_list:
        if i == min_positive_val:
            min_positive_val += 1
    return min_positive_val

print(find_missing(num_list3))
print(sort_nums(num_list3))
