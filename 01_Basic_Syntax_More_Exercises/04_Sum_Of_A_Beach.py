string = input()
case = string.upper()
result = case.count("SAND") + case.count("WATER") + case.count(
    "FISH") + case.count("SUN")
print(result)