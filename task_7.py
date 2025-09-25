n = int(input())
list = []
for i in range(n):
    nums = int(input(":"))
    list.append(nums)

list.sort()
i = 1
sum = 0
for i in range(len(list) - 1):
    sum += list[i]

print(sum)