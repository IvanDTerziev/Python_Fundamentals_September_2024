orders = int(input())
total_price = 0

for i in range(orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if price < 0.01 or price > 100 or days < 1 or days > 31 or capsules < 1 or capsules > 2000:
        continue

    price = price * days * capsules
    total_price += price
    print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')
