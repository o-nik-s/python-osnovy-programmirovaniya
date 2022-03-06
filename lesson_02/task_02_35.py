# Среднее значение последовательности

# Определите среднее значение всех элементов последовательности,
# завершающейся числом 0. Использовать массивы в данной задаче нельзя.
#
# Вводится последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит, а служит как признак
# ее окончания.
#
# Выведите ответ на задачу.

n = int(input())
mean = 0
i = 0
while n != 0:
    mean += n
    i += 1
    n = int(input())
mean /= i
print(mean)