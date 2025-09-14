
product = input()
qty = int(input())

def order_calculations(product_, quantity) :
    prices = {
        "coffee": 1.50,
        "coke": 1.40,
        "water": 1.00,
        "snacks": 2.00,
    }
    return prices[product_] * quantity

total_price = order_calculations(product, qty)
print(f'{total_price:.2f}')