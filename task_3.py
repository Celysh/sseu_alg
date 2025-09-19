from solution import solution,comp

variant = int(input('var: '))

exp1 = input('exp1: ')
exp2 = input('exp2: ')
exp3 = input('exp3: ')

b1 = str(input("b1: "))
b2 = str(input("b2: "))

if variant % 2 == 0:
    x = -5.0
    while x <= 5.0:
        y = solution(x,comp(x,b1,b2,exp1,exp2,exp3))
        print(f"{x:6.2f}\t\t{y:8.4f}")
        x += 0.5

else:
    x = -5.0
    while True:
        y = solution(x,comp(x,b1,b2,exp1,exp2,exp3))
        print(f"{x:6.2f}\t\t{y:8.4f}")
        x += 0.5
        if x > 5.0:
            break