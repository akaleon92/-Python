#Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного,
# итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

def count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
count_func(start_number = int(input("Введите начальное число: ")), stop_number = int(input("Введите конеченое число: ")))
cycle_func(my_list = [3, 7, 12, 'Text', 10], iteration = int(input("Введите количество итераций: ")))
