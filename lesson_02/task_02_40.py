# Числа Фибоначчи

# Последовательность Фибоначчи определяется так:
# F[0] = 0, F[1] = 1, ..., F[n] = F[n-1] + F[n-2].
# По данному числу n определите n-е число Фибоначчи F[n].

n = int(input())
if n == 0:
    Fn = 0
elif n == 1:
    Fn = 1
else:
    i = 2
    Fn1 = 0
    Fn2 = 1
    Fn = 1
    while i <= n:
        (Fn, Fn1, Fn2) = (Fn + Fn1, Fn, Fn1)
        i = i + 1
print(Fn)
