
def sorted_numbers(nums) :
    return sorted(nums)

numbers_as_string = input().split()
numbers_as_digits = []

for number in numbers_as_string :
      numbers_as_digits.append(int(number))

print(sorted_numbers(numbers_as_digits))

# Short syntax
# def sorted_numbers(numbers_as_string) :
#     numbers_as_digits = [int(num) for num in numbers_as_string.split()]
#     return sorted(numbers_as_digits)
#
# numbers_string = input()
#
# print(sorted_numbers(numbers_string))
