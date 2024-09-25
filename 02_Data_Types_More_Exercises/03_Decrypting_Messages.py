key = int(input())
lines = int(input())
result = []

for i in range(lines):
    char = input()
    result.append(chr(ord(char) + key))
print(''.join(result))