commands = {'coding', 'dog', 'cat', 'movie'}

coffees_needed = 0
while True:
    command = input()

    if command == 'END':
        break

    if command.lower() in commands:
        coffees_needed += 2 if command.isupper() else 1

if coffees_needed > 5:
    print('You need extra sleep')
else:
    print(coffees_needed)
