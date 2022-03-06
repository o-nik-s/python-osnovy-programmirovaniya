# Разность времен

# Даны два момента времени в пределах одних и тех же суток.
# Для каждого момента указан час, минута и секунда.
# Известно, что второй момент времени наступил не раньше первого.
#
# Определите сколько секунд прошло между двумя моментами времени.
#
# Программа на вход получает шесть целых чисел через перевод строки.
# Первые три целых числа соответствуют часам, минутам и секундам первого
# момента, следующие три числа соответствуют второму моменту.
#
# Часы задаются числом от 0 до 23 включительно. Минуты и секунды — от 0 до 59.
#
# Выведите число секунд между этими моментами времени.

h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

passTime = t2 - t1
print(passTime)
