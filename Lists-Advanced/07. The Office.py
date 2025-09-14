
def check_employee_hapiness(hapiness_list, factor):
    improved_hapiness = [current_value * factor for current_value in hapiness_list]
    average_hapiness = sum(improved_hapiness) / len(improved_hapiness)
    happy_count = sum(num >= average_hapiness for num in improved_hapiness)
    total_count = len(improved_hapiness)

    message = 'happy' if happy_count >= total_count / 2 else 'not happy'
    return f'Score: {happy_count}/{total_count}. Employees are {message}!'



hapiness_lst = list(map(int, input().split()))
hapiness_factor = int(input())
result = check_employee_hapiness(hapiness_lst, hapiness_factor)
print(result)