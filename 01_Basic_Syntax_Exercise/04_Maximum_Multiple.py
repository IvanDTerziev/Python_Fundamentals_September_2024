div = int(input())
bound = int(input())
current_number = bound
while not current_number % div == 0:
    current_number -= 1
print(current_number)