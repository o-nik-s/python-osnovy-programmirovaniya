# Стоимость покупки

# Пирожок в столовой стоит A рублей и B копеек.
# Определите, сколько рублей и копеек нужно заплатить за N пирожков.
# Программа получает на вход три числа:
# A, B, N — целые, неотрицательные, не превышают 10000.

A = int(input())
B = int(input())
N = int(input())

totalCost = (A * 100 + B) * N

print(totalCost // 100, totalCost % 100)