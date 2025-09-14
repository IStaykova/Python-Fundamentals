

def poli_integer(numbers_as_string) :
    current_num_list = []
    reversed_num_list = []

    for each_one in numbers_as_string.split(", "):
        current_num = int(each_one)
        reversed_num = int(str(current_num)[::-1])

        current_num_list.append(current_num)
        reversed_num_list.append(reversed_num)

    for a,b in zip(current_num_list, reversed_num_list):
        is_equal = a == b
        print(is_equal)

numbers_string = input()

poli_integer(numbers_string)