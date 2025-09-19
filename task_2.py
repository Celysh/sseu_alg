from solution import solution

a = float(input('Введите a: '))
b = float(input('Введите b: '))
exp = input('exp: ')
print(' x     | y')
print('---------------')
x = a
while x <= b + 0.05:
    y = solution(x,exp)
    print(f'{x:6.2f} | {y:6.3f}')
    x += 0.05