number_of_lines = int(input())
CAPACITY = 255
current_water = 0

for pour in range(number_of_lines):
    water = int(input())
    current_water += water
    if current_water > CAPACITY:
        print("Insufficient capacity!")
        current_water -= water

print(current_water)