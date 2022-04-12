# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

list_of_numbers = [10, 15, 3, 7]
k = 17


def gives_sum(nums_list, sum):
    for index, i in enumerate(nums_list):
        for j in nums_list[index + 1:]:
            if (i + j) == sum:
                return True
    return False


print(gives_sum(list_of_numbers, k))
