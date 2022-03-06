# Квадратное уравнение - 1

# Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
#
# Вводятся три действительных числа.
#
# Если уравнение имеет два корня, выведите два корня в порядке возрастания,
# если один корень — выведите одно число, если нет корней — не выводите ничего.


a = float(input())
b = float(input())
c = float(input())

epsilon = 5 * 10**-25

D = b**2 - 4 * a * c
if abs(D) < epsilon:
    x = -b / (2 * a)
    print(x)
elif D > epsilon:
    sqrtD = D ** (1 / 2)
    x1 = (-b - sqrtD) / (2 * a)
    x2 = (-b + sqrtD) / (2 * a)
    if x1 <= x2:
        print(x1, x2)
    else:
        print(x2, x1)