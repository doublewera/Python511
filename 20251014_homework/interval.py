# 1. Написать программу, в которой создается случайным образом два числа

from random import randint
a = randint(1, 10)
b = randint(1, 10)

# Лучше не полагаться на создание переменных в блоках кода
Bolsh = 0
Mensh = 0
if a > b:
    Bolsh = a
    Mensh = b
else:
    Bolsh = b
    Mensh = a

begunok = Mensh
# Продолжать, пока не превысим бОльшее
while begunok <= Bolsh:
    print(begunok)
    begunok += 1   # begunok = begunok + 1

# Программа должна вывести на экран все числа от меньшего до большего включительно
# Нельзя: for, range, max
# Можно: while, if

# пример: случайно попались числа 14, 9
# Вывести:
# 9
# 10
# 11
# 12
# 13
# 14