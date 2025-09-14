
def round_numbers(num_as_string):
    numbers = num_as_string.split(" ")
    rounded = []
    for num in numbers:
        rounded.append(round(float(num)))
    return rounded

strings = input()

print(round_numbers(strings))

