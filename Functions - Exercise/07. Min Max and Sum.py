

def min_max_sum (numbers_as_string) :
    numbers_as_digits = [int(num) for num in numbers_as_string.split()]
    print(f'The minimum number is {min(numbers_as_digits)}')
    print(f'The maximum number is {max(numbers_as_digits)}')
    print(f'The sum number is: {sum(numbers_as_digits)}')

numbers_string = input()

min_max_sum(numbers_string)