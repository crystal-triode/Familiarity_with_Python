# 3.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(map(float, input("Введите числа через пробел:\n").split()))
lst1 = [round(i%1,2) for i in lst if i%1 != 0]
print(max(lst1) - min(lst1))
