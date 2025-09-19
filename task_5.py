from solution import solution

mult1= int(input("1: "))
mult2= int(input("2: "))

exp = input('exp :')
sum = 0

for i in range(mult1, mult2 + 1):
    sum += float(solution(i, exp))
    i += 1

print(sum)