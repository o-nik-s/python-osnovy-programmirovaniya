# Сколько совпадает чисел
#
# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).

a = int(input())
b = int(input())
c = int(input())
count = 0
if a == b:
    count = 2
    if a == c:
        count = 3
elif b == c or a == c:
    count = 2
print(count)