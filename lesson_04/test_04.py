def rec():
    n = int(input())
    if n != 0:
        if n % 2 == 0:
            print(n)  # Четные числа просто берем и печатаем
        # Нечетные сразу печатать не должны, в начале нам нужны лишь четные
        rec()  # Поэтому вызываем следующий экземпляр функции
        if n % 2 != 0:
            print(n)  # Если нечетное, то потом его уже печатаем


rec()