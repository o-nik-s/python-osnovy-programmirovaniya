# Квартиры
# В доме несколько подъездов. В каждом подъезде одинаковое количество квартир.
# Квартиры нумеруются подряд, начиная с единицы. Может ли в некотором подъезде
# первая квартира иметь номер x, а последняя – номер y?
#
# Вводятся два натуральных числа x и y (x≤y), не превышающие 10000.
# Выведите слово YES (заглавными латинскими буквами), если такое возможно,
# и NO в противном случае.

x = int(input())
y = int(input())

quant = y - x + 1
if (x - 1) % quant == 0 and y % quant == 0:
    print("YES")
else:
    print("NO")
