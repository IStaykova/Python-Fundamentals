
# def round_numbers(num_as_string):
#     numbers = num_as_string.split(" ")
#     rounded = []
#     for num in numbers:
#         rounded.append(round(float(num)))
#     return rounded
#
# strings = input()
#
# print(round_numbers(strings))

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

smallest_num = lambda num_1, num_2, num_3: min(num_1, num_2, num_3)
print(smallest_num(number_1,number_2,number_3))