quantity = int(input())
days = int(input())

budget = 0
total_spirits = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget -= 2 * quantity
        total_spirits += 5
    if day % 3 == 0:
        budget -= 5 * quantity + 3 * quantity
        total_spirits += 13
    if day % 5 == 0:
        budget -= 15 * quantity
        total_spirits += 17
        if day % 3 == 0:
            total_spirits += 30
    if day % 10 == 0:
        total_spirits -= 20
        budget -= 5 + 3 + 15

if days % 10 == 0:
    total_spirits -= 30

print(f"Total cost: {abs(budget)}")
print(f"Total spirit: {total_spirits}")