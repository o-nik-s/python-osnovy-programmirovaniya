# Количество нулей

# Дано несколько чисел. Подсчитайте, сколько из них равны нулю,
# и выведите это количество.
#
# Cначала вводится число N, затем вводится ровно N целых чисел.
# Выведите ответ на задачу.

N = int(input())
count = 0
for i in range(1, N + 1):
    if int(input()) == 0:
        count += 1
print(count)
