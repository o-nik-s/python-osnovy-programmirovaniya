# Неделя 4

# Функции

# Особенности человеческого мышления в том, что человек не может сразу
# осознать большую задачу, и нужно ее разбить на более мелкие части.

# Функции - части программы, которые можно повторно вызывать с разными
# параметрами, чтобы не писать много раз одно и то же. Функции в
# программировании немного отличаются от математических функций. В математике
# функции могут только получить параметры и дать ответ, в программировании же
# функции умеют делать что-нибудь полезное, например, ничего не возвращать,
# но что-то печатать.

# Функции чрезвычайно полезны, если одни и те же действия нужно выполнять
# несколько раз. Но некоторые логические блоки работы с программой иногда тоже
# удобно оформлять в виде функции. Это связано с тем, что человек может
# одновременно держать в голове ограниченное количество вещей. Когда программа
# разрастается, отследить все уже очень сложно. В пределах одной небольшой
# функции запутаться гораздо сложнее - известно, что она получает на вход, что
# должна выдать, а об остальной программе в это время можно не думать.

# В программировании также считается хорошим стилем писать функции,
# умещающиеся на один экран. Тогда можно одновременно окинуть взглядом всю
# функцию и не нужно крутить текст туда-сюда. Поэтому, если получилось что-то
# очень длинное, то нужно нарезать его на кусочки так, чтобы каждый из них был
# логичным (делал какое-то определенное действие, которое можно назвать) и не
# превышал при этом 10-15 строк.

# Мы уже использовали готовые функции, такие как print, len и некоторые
# другие. Эти функции описаны в стандартной библиотеке или других подключаемых
# библиотеках.

# Функции так же могут не принимать параметров.

def hypor(a, b):  # Определение функции
    sqrSum = a**2 + b**2
    return sqrSum**(1/2)  # Возврат значения функции


# Использование функций

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def cnk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

print(factorial(5))
print(cnk(25, 7))

# Step into my code...
# Только внутри моего кода, не заходя в код Питона


# Возврат значений

def max2(a, b):
    if a > b:
        return a
    return b  # Поскольку return a возвращает значение и прерывает функцию

# Иногда чтобы выйти из вложенного цикла, оборачивают циклы в функцию,
# и как только нужно выйти из вложенного цикла, делают return из функции.


# Функция может передаваться в качестве аргумента!!! - из книги "Think Python"


# Возврат нескольких значений из функции - через запятую
def sort2(a, b):
    if a < b:
        return a, b
    else:
        return b, a
a = int(input())
b = int(input())
minimum, maximum = sort2(a, b)
print(minimum, maximum)

# Возврат логических значений
def isEven(n):
    return n % 2 == 0


'''# Из книги "Think Python" о параметре функции в виде функции
Упражнение 3.4
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
do_twice(print_spam)
'''


# Локальные и глобальные переменные
#
# Переменные, значения которых изменяются внутри функции по умолчанию
# считаются локальными, т.е. доступными только внутри функции. Как только
# функция заканчивает свою работу, то переменная уничтожается.


# Эта программа завершится с ошибкой builtins. UnboundLocalError: local
# variable 'a' referenced before assignment (обращение к переменной до
# инициализации). Любое присваивание значения переменной внутри тела функции
# делает переменную локальной.
def f():
    print(a)
    if False:
        a = 0
a = 1
f()


# С помощью специальной команды global можно сделать так, что функция сможет
# изменить значение глобальной переменной. Для этого нужно записать в начале
# функции слово global, а затем через запятую перечислить имена глобальных
# переменных, которые функция сможет менять. Например, такой код:
def f():
    global a  # Описываем переменную как глобальную и теперь можем ее менять!
    a = 1
    print(a, end=' ')
a = 0
f()
print(a)
# выведет "1 1", т.к. значение глобальной переменной будет изменено внутри функции.

# Все параметры функции являются локальными переменными со значениями, которые
# были переданы в функцию. Параметры также можно изменять и это никак не
# повлияет на значения переменных в том месте, откуда была вызвана функция
# (если тип объектов-параметров был неизменяемым).-

# Bспользование глобальных переменных внутри функций в данном курсе строго запрещено.
# Все нужное для работы функции должно передаваться в качестве параметров.

# Глобальные переменные - видны из любого места программы.



# Рекурсия

# Рекурсия - это вызов функцией самой себя.

# Дана последовательность чисел до нуля. Требуется вывести ее задом наперед.
def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)
rec()

# Экземпляр функции имеет свои параметры и помнит то место, в которое нужно вернуться после того,
# как он закончит свою работу.

# Рекурсия предназначена для решения каких-то задач, где можно часть работы
# поручить другому. Т.е. общий подход такой: проверяем, не пора ли заканчивать
# действия в рекурсивной функции; выполняем действия, которые должен сделать
# этот экземпляр; поручаем все остальные действия другим экземплярам функции.

def reverse():
    n = int(input())
    if n != 0:
        reverse()
        print()


# В рекурсии всегда нужно проверять в самом начале функции условие окончания обработки.


# Первый экземпляр функции, в свою очередь, еще не закончит последовательность
# рекурсивных вызовов, а вызовет второй экземпляр, который, в свою очередь,
# будет хранить свою локальную переменную и место, куда нужно вернуться.

# Стек — это значит, что мы кладем только наверх, как стопка книг, например,
# такая, и снимать можем столько сверху, из середины выдернуть не можем. Такая
# абстракция очень хорошо описывает как раз процесс запуска функции, у нас
# всегда активный экземпляр лежит сверху, и когда мы его заканчиваем, убираем
# ровно одну штуку и попадаем в то место, где мы должны продолжать работу.



# Использование рекурсии

# Рассмотрим задачу, где действия выполняются как на рекурсивном подъёме, так и на рекурсивном спуске.
# Пусть хотим в последовательности, заканчивающейся нулем, в начале вывести все четные функции,
# а затем - все нечетные функции в обратном порядке.

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


'''Общая схема написания рекурсивных функций: сначала проверяется условие, 
когда функция должна закончиться, а дальше делается все остальное. При этом 
параметр должен сходиться к значению базы. Обычно это означает, что при каждом 
следующем вызове рекурсии параметр должен уменьшаться.'''

