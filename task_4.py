from solution import solution

sum1= int(input("1: "))
sum2 = int(input('2: '))
exp = input('exp :')
sum = 0
for i in range(sum1, sum2 + 1):
    sum += float(solution(i, exp))
    i += 1

print(sum)