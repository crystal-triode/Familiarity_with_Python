# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o	45 -> 101101
# o	3 -> 11
# o	2 -> 10


n = int(input('Введите целое число: ')) 
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(f'Двоичное число: {b}')