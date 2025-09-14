
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(nums_1, nums_2):
    return nums_1 + nums_2

def subtract(sum_result, nums_3):
    return sum_result - nums_3

def add_and_subtract(nums_1, nums_2, nums_3):
    return subtract(sum_numbers(nums_1, nums_2), nums_3)

print(add_and_subtract(num_1, num_2, num_3))