
num_list = list(map(int, input().split(", ")))

found_indices = map(
    lambda x: x if num_list[x] % 2 == 0 else 'no',
    range(len(num_list))
)

even_indices = list(filter(lambda a: a != 'no', found_indices))
print(even_indices)