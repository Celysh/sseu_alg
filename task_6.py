n = int(input())

max1 = max2 = float('-inf')
min1 = min2 = float('inf')

for i in range(n):
    nums = int(input(':'))
    if nums > max1:
        max2 = max1
        max1 = nums
    elif nums > max2:
        max2 = nums
    if nums < min1:
        min2 = min1
        min1 = nums
    elif nums < min2:
        min2 = nums

print(f'result: {max2} - {min2} = {max2 - min2}')