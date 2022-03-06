# Наименьшее расстояние между локальными максимумами

# Определите наименьшее расстояние между двумя локальными максимумами
# последовательности натуральных чисел, завершающейся числом 0. Локальным
# максимумом называется такое число в последовательности, которое больше
# своих соседей. Если в последовательности нет двух локальных максимумов,
# выведите число 0. Начальное и конечное значение при этом локальными
# максимумами не считаются.

n = int(input())
length = 0
locMax = n
sign = 0
nLocMax = 0
dist = 0  # Расстояние между локальными максимумами
k = 0  # Номер в последовательности локального максимума
while n != 0:
    if n > locMax:
        locMax = n
        sign = 1
    elif n == locMax:
        sign = 0
    elif n < locMax:
        if sign == 1:
            # print("Новый локальный максимум", locMax, "на позиции", k)
            if nLocMax > 0 and (dist == 0 or k - nLocMax < dist):
                dist = k - nLocMax
                # print("Новая дистанция между локальными максимумами:", dist)
            nLocMax = k
        locMax = n
        sign = -1
    n = int(input())
    k += 1
print(dist)