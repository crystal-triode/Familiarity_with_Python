# 4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from calendar import c
import os
os.system("cls")
from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))

ratio_list = list([randint(0, 101) for i in range(k+1)]) 
if ratio_list[0] == 0: 
    ratio_list[0] = randint(1, 101)
print(ratio_list)

def get_polynomial(k, ratio_list): 
    str1 = ['*x**']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
    print(polynomial)
    for x in polynomial:
        x.append(' + ') 
    polynomial = list(itertools.chain(*polynomial)) 
    print(polynomial)
    polynomial[-1] = ' = 0' 
    return "".join(map(str, polynomial)).replace(' 1*x',' x') 

list = get_polynomial(k, ratio_list)
print(list)

with open('HomeTask_4_4.txt', 'w') as data:
    data.write(list)
with open('HomeTask_4_42.txt', 'w') as data:
    data.write(list)
