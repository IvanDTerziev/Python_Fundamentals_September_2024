budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = 0.75 * price_1kg_flour
price_1l_milk = 1.25 * price_1kg_flour / 4  # директно делим на 4, тъй като използваме само 1/4 от литъра
cozonac_price = price_1kg_flour + price_1pack_eggs + price_1l_milk
cozonacs_count = 0
colored_eggs = 0

while budget >= cozonac_price:
    budget -= cozonac_price
    cozonacs_count += 1
    colored_eggs += 3
    if cozonacs_count % 3 == 0:
        colored_eggs -= cozonacs_count - 2

print(f"You made {cozonacs_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
