forbidden_symbols = [',', '.', '_']
nums = int(input())

for i in range(nums):
    string = input()
    for sym in forbidden_symbols:
        if sym in string:
            print(f'{string} is not pure!')
            break
    else:
        print(f'{string} is pure.')