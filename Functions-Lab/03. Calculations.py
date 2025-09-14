
operator = input()
num_a = int(input())
num_b = int(input())

def make_calculations(operand,a,b):
    result = 0
    if operand == "multiply":
        result = a * b
    elif operand == "divide":
        result = int(a / b)
    elif operand == "add":
        result = a + b
    elif operand == "subtract":
        result = a - b
    return result
print(make_calculations(operator, num_a, num_b))