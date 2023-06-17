# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Элементов в первом наборе: '))
m = int(input('Элементов во втором наборе: '))
listN = []
listM = []
for i in range(n):
    listN.append(int(input(f'Значение {i} элемента: ')))
for i in range(m):
    listM.append(int(input(f'Значение {i} элемента: ')))
setN = set(listN)
setM = set(listM)
setMN = setN.intersection(setM) ## функция сразу сортирует значения
listMN = list(setMN)
# for i in range(0,len(listMN)):
#     for j in range(i+1,len(listMN)):
#         if listMN[j]< listMN[i]:
#             min = listMN[j]
#             listMN[j] = listMN[i]
#             listMN[i] = min
print(listMN)