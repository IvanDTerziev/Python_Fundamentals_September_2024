num = input()

num_list = []
for i in range(len(num)):
     num_list.append(int(num[i]))
num_list.sort(reverse=True)
print(*num_list, sep="")