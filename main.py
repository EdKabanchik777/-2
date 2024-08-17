import random


def test(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password = password + str(i) + str(j)
    return password


n = int(input('Введите число от 1 до 20: '))
if 1 <= n <= 20:
    res = test(n)
    print(res)
else:
    print('Число не подходит')
