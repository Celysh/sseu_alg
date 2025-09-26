n = int(input())
list = []
max1 = float('-inf')
min1 = float('inf')

for i in range(n):
    nums = int(input(':'))
    if nums > max1:
        max1 = nums
    if nums < min1:
        min1 = nums
    list.append(nums)

h = list.index(min1)
sum = 0
while h < list.index(max1):
    sum += list[h]
    h += 1
print(sum)
