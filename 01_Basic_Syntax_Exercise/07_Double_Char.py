while True:
    string = input()
    if string == 'End':
        break

    if string == 'SoftUni':
        continue

    print(''.join(char * 2 for char in string))
