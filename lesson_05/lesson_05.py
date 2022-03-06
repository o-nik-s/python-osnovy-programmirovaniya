# Кортежи, цикл for, списки

# Кортежи и списки нужны для хранения большого объекма данных

# Кортеж - tuple

myTuple = (1, 2, 3)
print(myTuple[1])
# Нумерация так же с нуля

# Кортеж предназначен для хранения чего угодно не изменяемого
# Для изменяемых значений используются списки

sTuple = (4, 5, 6)
print(myTuple + sTuple)
# В итоге одни элементы добавляются к другим элементам. Точно так же как и со строками.

print(len(myTuple))

# В кортежах можно хранить объекты совершенно разной природы
myTuple = (1, 3.14, 'abc')
print(myTuple)

# В качестве элемента кортежа может выступать... кортеж
myTuple = (1, (2, 3), (4))
print(myTuple)

# (4) - это просто число
# (4,) - кортеж их одного элемента - синглтон
myTuple = (1, (2, 3), (4,))
print(myTuple)


print(myTuple[1][0])
# Когда несколько индексов в скобках, в начале пишем наиболее внешний, а затем внутренний

# Таким способом можно сделать что-то вроде таблицы со строками и столбцами

# Кортежи еще применяются для описания каких-то объектов
# Например, мы хотим сделать описание человека из его имени, фамилии, возраста

man = {'Ivan', 'Ivanov', 28}

# Так же как и со строками, можно обращаться по отрицательным элементам

# Таким образом, кортежти используются для описания сложной струкуры, состоящей из разных типов полей

# И, вообще говоря, любой элемент кортежа является просто ссылкой на какой-то объект. Т.е. все элементы состоят из ссылок.


# Упаковка и распаковка кортежей

# Упаковка кортежа
# Скобки можно опускать, если нет никаких действий и пр.
myTuple = 1, 2, 3
# Три числа будут интерпретированы как запись константного кортежа и будут интерпретированы в один кортеж

a, b, c = myTuple
# Распаковка кортежа - разложение элементов кортежа по переменным
# В таком выражении справа должен находится кортеж той же длины

print(b)

'''По аналогии со строками, которые могут хранить в себе отдельные символы, в языке Питон 
существует тип кортеж, который позволяет хранить в себе произвольные элементы.
Кортеж может состоять из элементов произвольных типов и является неизменяемым типом, 
т.е. нельзя менять отдельные элементы кортежа, как и символы строки. Константные кортежи 
можно создавать в программе, записывая элементы через запятую и окружая скобками. Например, 
testTuple = (1, 2, 3). В случае, если кортеж является единственным выражением слева или справа 
от знака присваивания, то скобки могут быть опущены. Во всех остальных случаях скобки опускать 
не следует - это может привести к ошибкам.

Многие приемы и функции для работы со строками также подходят и для кортежей.

В случае сложения кортежей создается новый кортеж, который содержит в себе элементы сначала 
из первого, а затем второго кортежа (точно также как и в случае со строками). Также кортеж 
можно умножить на число, результат этой операции аналогичен умножению строки на число.

К кортежу можно применять функцию len и обращаться к элементам по индексу (в том числе 
по отрицательному) также как и к строкам.

В одном кортеже могут храниться элементы различных типов, например, строки, числа и другие 
кортежи вперемешку. Например, в кортеже myTuple = (('a', 1, 3.14), 'abc', ((1), (2, ))), 
myTuple[0] будет кортежем ('a', 1, 3.14), myTuple[1] строкой 'abc', а myTuple[2] кортежем 
состоящим из числа 1 и кортежа из одного элемента (2, ). Числа, записанные в скобках, 
интерпретируются как числа, в случае возникновения необходимости создать кортеж из одного 
элемента необходимо после значения элемента написать запятую. Если вывести myTuple[2][1], 
то напечатается (2,), а если вывести myTuple[2][1][0], то будет напечатано число 2.

Кортеж, содержащий в себе один элемент, называется синглтоном. Как и к строкам, 
к кортежам можно применять операцию среза с тем же смыслом параметров. Если в срезе 
один параметр, то будет возвращена ссылка на элемент с соответствующим номером. Например, 
print((1, 2, 3)[2]) напечатет 3. Если же в срезе более одного параметра, то будет 
сконструирован кортеж, даже если он будет синглтоном. Например, в случае вызова 
print((1, 2, 3)[1:]) будет напечатно (2, 3), а в случае вызова print((1, 2, 3)[2:]) 
будет напечатан синглтон (3,).

Кортежи, обычно, предназначаются для хранения разнотиповых значений, доступ к которым 
может быть получен в результате обращения по индексу или с помощью операции распаковки.

Распаковкой называется процесс присваивания, в котором кортеж, составленный из отдельных 
переменных находится в левой части выражения. В таком выражении справа должен находится 
кортеж той же длины. Например, в результате выполнения такого кода:'''
manDesc = ("Ivan", "Ivanov", 28)
name, surname, age = manDesc
'''В переменной name кажется ''Ivan'', в surname - ''Ivanov'', а в переменной age число 28. 
На английском распаковка кортежа называется tuple unpacking.'''


# Обмен значений
a = 1
b = 2
a, b = b, a  # Кортежу присвоили кортеж
print(a, b)
# Создается кортеж с двумя переменными, оно упаковывается в один объект, а затем происходит распоковка объекта

a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)


# Функция range, цикл for

# Итерируемые объекты
# Это объекты, с которыми можно поочередно вытаскивать какие-то значения

# Например, мы хотим досчитать до миллиарды

# В памяти займет слищком много места
# Достаточно знать текущий объект и правило, по которому можно получить следующий

# Итератор - знает правило, по которому получается следующий элемент

myRange = range(100)  # iterable
# Начальный объект - 0, правая граница не включается

print(type(myRange))

print(tuple(myRange))
# tuple вытаскивает все объекты по одному

# iterable - Это не только правило, но и кортеж является iterable
# Строка тоже является итерируемым типом

print(tuple('abcde'))

# Для перебора всех элементов чего-либо итерируемого /range, строка, кортеж/ существует список for

for color in ('red', 'green', 'yellow'):
    print(color, 'apple')

# Часто for применяется для перебора чисел, которые мы умеем генерировать с помощью range()

for i in range(25):
    print(i)


# Существует так же range с двуми или тремя параметрами

for i in range(10, 21):
    print(i, end=' ')
# Правая граница не включается

# Шаг по умолчанию равен 1

for i in range(10, 21):
    print(i, end=' ')


# Пусть мы хотим посчитать все нечетные числа
for i in range(1, 30, 2):
    print(i, end=" ")

# Если надо посчитать справа налево, то range с тремя параметрами
for i in range(10, -1, -1):
    print(i, end=" ")

print()
print()

# Таблица умножения
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print()

# iterable: к элементам которых можно получать последовательный доступ

# Также существует range с тремя параметрами range(from, to, step),
# который сгенерирует iterable с числами от from, не превышающие to с шагом изменения step.

# Во многом параметры range напоминают значения параметров в срезах строк.

# В общем случае цикл for выглядит так for имяПеременной in нечтоИтерируемое:

# Все действия, которые должны выполняться в for, должны выделяться отступом,
# как и в if или while. Работа цикл for может быть прервана с помощью команды break
# или может быть осуществлен переход к следующей итерации с помощью continue. Эти команды
# имеют тот же эффект, что и при работе с циклом while.


'''
1	Вы не можете добавлять элементы в кортеж. У кортежей нет методов append и extend.
2	Вы не можете удалять элементы из кортежа. У кортежей нет методов remove и pop.
3	Вы не можете искать элементы в кортеже с помощью метода index — у кортежей нет такого метода.
4	Однако, вы можете проверить наличие элемента в кортеже с помощью оператора in.
http://ru.diveintopython.net/odbchelper_tuple.html'''

'''Кортежи в Python имеют совсем немного методов.
Если быть точным их всего два: index() и count().'''


'''---------------------------------------------------------------------------------------------------'''


'''Списки'''
# Списки

# /=массив в других языках/
# Можно поменять значение элемента
# Т.е. это первый изменяемый тип, который мы изучаем

a = [1, 2, 3]  # Квадратные скобки опускать нельзя, потому как иначе будет интерпретирован как кортеж
# Любая переменная в Питоне является ссылкой на какой-то объект

b = a  # Ссылка будет показывать на тот же самый объект, что и a

# Из-за того, что объект изменяемый, возможны разные интересные вещи:
a[0] = 5 # Изменение объекта, обращаемся как с переменной
print(a)
print(b)

# Если меняем a, то меняется и b, потому что a и b - лишь ссылки на один и тот же объект

# Простой способ сделать копию списка - это сделать срез, содержащий все элементы списка
b = a[:]

# Когда мы делаем срез, у нас в любом случае генерируется новый объект в памяти
a[1] = 0
print(a, b)

# Если объекты не изменяемы, то две ссылки могут показывать на один и тот же объект
a = [1, 2, 3]

# Если объект изменяемый, то обязательно создается копия объекта в памяти
b = [1, 2, 3]
a[0] = 4
print(b) # Не изменилось!

# Единственный допустимый тип данных для списка - это ссылка /на какой-то объект/

a = [1, [1, 3, 'a'], [5, [5, 6.7]]]
# Внутри может быть все, что угодно
print(a)

# Главное, что нужно знать, абсолютно любой объект - это ссылка.
# Т.е. изменение, отсчет и пр. - это все делаем со ссылками


def replaceFirst(fList):
    fList[0] = 0

a = [1, 2, 3]
replaceFirst(a)
print(a)

# В функцию передается ссылка на объект в качестве параметра

# В нашем случае передавалась ссылка на список
# Список является изменяемым объектом, поэтому изменяется везде


def replaceFirst(fList):
    fList = fList[::-1]  # Хотим положить развернутый список
    # Локальная переменная изменилась, но после выхода из функции уничтожилось

a = [1, 2, 3]
replaceFirst(a)
print(a)
# То, что передается в функцию, по прежнему измениться не может!

# Т.е. пройдя по ссылке на изменяемый объект, изменить можно, а саму функцию изменить нельзя

# Т.е. функция может изменять параметры, но делать это не желательно
# Изменять таким образом списки нельзя


'''Список в Питоне является аналогом массивов в других языках программирования. 
Список - это набор ссылок на объекты (также как и кортеж), однако он является изменяемым.

Константные списки записываются в квадратных скобках, все остальное в них аналогично 
кортежам. Например, можно создать список с числами от 1 до 5: myList = [1, 2, 3, 4, 5].

Списки и кортежи легко преобразуются друг в друга. Для преобразования списка в кортеж 
надо использовать уже известную нам функцию tuple, а для преобразования кортежа в список 
нужна функция list. Также функцию list можно применить к строке. В результате этого 
получится список, каждым элементом которого будет буква из строки. Так list('abc') 
будет выглядеть как ['a', 'b', 'c'].

К спискам также применима функция len и срезы, которые работают также как в кортежах.

Главным отличием списка от кортежа является изменяемость. То есть можно взять 
определенный элемент списка и изменить его (он может быть в левой части операции 
присваивания).'''

myList = [1, 2, 3]
myList[1] = 4
print(myList)

''' Изменение символа (или элемента в кортеже) можно было реализовать, 
сделав два среза и конкатенация первой части строки, нового символа и "хвоста" строки. 
Это очень медленная операция, время ее выполнения пропорционально длине строки. Замена 
элемента в списке осуществляется за O(1), т.е. не зависит от длины списка.'''


'''Изменение списков'''

'''Список, как и другие типы в языке Питон, является ссылкой на список ссылок. 
При этом список является изменяемым объектом, т.е. содержимое по этой ссылке 
может поменяться.'''

a = [1, 2]
b = a
b[0] = 3
print(a)

'''В результате выполнения этой программы будет напечатано [3, 2]. Это связано 
с тем, что присваивание в Питоне - это просто "привязывание" нового "ярлычка" 
к объекту. После присваивания b = a обе ссылки начинают показывать на один 
и тот же объект и если он измененен по одной ссылке, то по второй ссылке 
он тажке будет доступен в измененном состоянии.'''

'''Если же написать такой код:'''
a = [1, 2]
b = [1, 2]
a[0] = 3
print(b)
'''то будет выведено [1, 2]. Несмотря на то, что объекты имеют одинаковое значение 
из-за их мутабельности (изменяемости) для каждого значения будет создан отдельный 
объект и ссылки a и b будут показывать на разные объекты. Изменение одного из них, 
естетственно, не приводит к изменению другого.'''

'''В результате выполнения такого кода:'''
a = [1, 2]
b = a
a = [3, 4]
print(b)
'''будет выведено [1, 2]. Сначала в памяти создается объект [1, 2] и к нему 
привязывается ссылка a, затем к тому же объекту привязывается ссылка b, а затем 
создается новый объект [2, 3], к которому привязывается ссылка a (отвязавшись 
от своего предыдущего значения). При этом ссылка b не изменилась (она может 
измениться только если b будет участвовать в левой части присваивания) 
и по-прежнему показывает на [1, 2].'''

'''Если списки переданы в функцию в качестве параметров, то их содержимое также может быть 
изменено этой функцией:'''
def replaceFirst(myList):
    myList[0] = 'x'

nowList = list('abcdef')
replaceFirst(nowList)
print(nowList)

'''Выводе этой программы будет ['x', 'b', 'c', 'd', 'e', 'f'].

Однако, сама ссылка внутри функции не может быть изменена, если она передана как параметр функции. 
Рассмотрим пример:'''


def reverseList(funcList):
    funcList = funcList[::-1]

mainList = list('abc')
reverseList(mainList)
print(mainList)

'''Эта программа не развернет список, т.е. вывод будет ['a', 'b', 'c'].

Здесь в основной программе конструируется объект ['a', 'b', 'c'] и к нему привязывается ссылка mainList. 
При передаче mainList в качестве параметра в функцию создастся еще одна ссылка funcList, 
показывающая на объект ['a', 'b', 'c']. В результате применения среза создастся новый объект ['c', 'b', 'a'] 
и ссылка funcList начнет указывать на него. Однако, значение ссылки mainList при этом не изменится и со значениями 
по ссылке mainList также ничего не произойдет (напомним, что операция среза создает новый объект, не изменяя старый).'''


'''Список в Питоне является аналогом массивов в других языках программирования. Список - это набор ссылок 
на объекты (также как и кортеж), однако он является изменяемым.

Константные списки записываются в квадратных скобках, все остальное в них аналогично кортежам. 
Например, можно создать список с числами от 1 до 5: myList = [1, 2, 3, 4, 5].

Списки и кортежи легко преобразуются друг в друга. Для преобразования списка в кортеж надо 
использовать уже известную нам функцию tuple, а для преобразования кортежа в список нужна функция list. 
Также функцию list можно применить к строке. В результате этого получится список, каждым элементом 
которого будет буква из строки. Так list('abc') будет выглядеть как ['a', 'b', 'c'].

К спискам также применима функция len и срезы, которые работают также как в кортежах.

Главным отличием списка от кортежа является изменяемость. То есть можно взять определенный элемент списка 
и изменить его (он может быть в левой части операции присваивания).'''

myList = [1, 2, 3]
myList[1] = 4
print(myList)

'''Изменение символа (или элемента в кортеже) можно было реализовать, сделав два среза и конкатенация 
первой части строки, нового символа и "хвоста" строки. Это очень медленная операция, время ее выполнения 
пропорционально длине строки. Замена элемента в списке осуществляется за O(1), т.е. не зависит от длины списка.'''

'''Изменение списков

Список, как и другие типы в языке Питон, является ссылкой на список ссылок. При этом список является 
изменяемым объектом, т.е. содержимое по этой ссылке может поменяться. рассмаотрим такой пример:'''
a = [1, 2]
b = a
b[0] = 3
print(a)

'''В результате выполнения этой программы будет напечатано [3, 2]. Это связано с тем, что присваивание 
в Питоне - это просто "привязывание" нового "ярлычка" к объекту. После присваивания b = a обе ссылки 
начинают показывать на один и тот же объект и если он измененен по одной ссылке, то по второй ссылке 
он тажке будет доступен в измененном состоянии.'''

'''Если же написать такой код:'''
a = [1, 2]
b = [1, 2]
a[0] = 3
print(b)
'''то будет выведено [1, 2]. Несмотря на то, что объекты имеют одинаковое значение из-за их мутабельности 
(изменяемости) для каждого значения будет создан отдельный объект и ссылки a и b будут показывать 
на разные объекты. Изменение одного из них, естетственно, не приводит к изменению другого.'''

'''В результате выполнения такого кода:'''
a = [1, 2]
b = a
a = [3, 4]
print(b)
'''будет выведено [1, 2]. Сначала в памяти создается объект [1, 2] и к нему привязывается ссылка a, 
затем к тому же объекту привязывается ссылка b, а затем создается новый объект [2, 3], к которому 
привязывается ссылка a (отвязавшись от своего предыдущего значения). При этом ссылка b не изменилась 
(она может измениться только если b будет участвовать в левой части присваивания) и по-прежнему 
показывает на [1, 2].'''

'''Если списки переданы в функцию в качестве параметров, то их содержимое также может быть изменено этой функцией:'''
def replaceFirst(myList):
    myList[0] = 'x'

nowList = list('abcdef')
replaceFirst(nowList)
print(nowList)
'''Выводом этой программы будет ['x', 'b', 'c', 'd', 'e', 'f'].'''

'''Однако, сама ссылка внутри функции не может быть изменена, если она передана как параметр функции. Рассмотрим пример:'''
def reverseList(funcList):
    funcList = funcList[::-1]

mainList = list('abc')
reverseList(mainList)
print(mainList)
'''Эта программа не развернет список, т.е. вывод будет ['a', 'b', 'c'].
Здесь в основной программе конструируется объект ['a', 'b', 'c'] и к нему привязывается ссылка mainList. 
При передаче mainList в качестве параметра в функцию создастся еще одна ссылка funcList, показывающая 
на объект ['a', 'b', 'c']. В результате применения среза создастся новый объект ['c', 'b', 'a'] 
и ссылка funcList начнет указывать на него. Однако, значение ссылки mainList при этом не изменится 
и со значениями по ссылке mainList также ничего не произойдет (напомним, что операция среза создает 
новый объект, не изменяя старый).'''



'''Методы split и join'''

'''Как списки и строки связаны между собой'''

'''Создание списка из строки
a = list(итерируемое)
Строка является итеритуемым объектом, т.е. если передали строку, получится список со всеми элементами.'''
a = list('abcde')
print(a)
'''Если нам нужно что-то большое изменить в строке, то можно взять строку, сделать из нее список, 
что-то изменить и собрать строку обратно.'''
a[0] = 'f'

'''Хотим собрать строку обратно'
Метод join.
Мы указываем строку-разделитель. В нашем случае мы хотим просто склеить все буквы без разделителей, поэтому
пишем ''. Далее вызываем метод join, который принимает в качестве параметра список строк, которые нужно
объединить.'''
# Разделитель.join(Имя_Списка)
a = ''.join(a)
print(a)

'''Очень часто нужно считать список слов /разделенные пробелом последовательности непробельных символов/'''
'''Метод slip()'''
wordList = input().split()
print(wordList)

'''Если резать только по чему-то одному, то указываем параметр'''
# wordList = input().split(' ') - по пробелам
wordList = input().split('a')
print(wordList)
# По умолчанию: пробелы, табуляция, переводы строки

'Теперь нужно получить список чисел /записанных в одну строку/'
'''Функция map: функция, позволяющая применить некоторую функцию к каждому объекту списка'''
# map(имя_функции, список)
intList = list(map(int, input().split()))
print(intList)
# Хотим вывести числе через пробел
# print(' '.join(intList))
print(' '.join(map(str, intList)))


# Для печати списка чисел / строк существует специальная конструкция Звездочка
print(*intList)  # Печатает все элементы списка /чисел, строк/ через пробел


'''Строки имеют два полезных метода, которые пригодятся при работе со списками.

Метод split позволяет разрезать строку (string) на отдельные слова ("токены"). 
В качестве разделителя может выступать пробел, символ табуляции или перевода строки. 
Этот метод не изменяет строку и возвращает список строк-токенов.'''
print('red green        blue'.split())

'''Чтобы научиться читать числа из одной строки нужно научиться еще одной функции - map. 
Функция map принимает два параметра: первый это функции, а второй - iterable элементов, 
к которому нужно применить эту функцию. В результате получается iterable с результатом 
применения функции к каждому элементу списка параметра.'''
print(list(map(len, ['red', 'green', 'blue'])))

'''Метод split в сочетании с функцией map удобно использовать для считывания списка чисел, 
записанных в одну строку и разделенных пробелами.'''
numList = list(map(int, input().split()))

'''Сначала осуществляется считывание строки, затем выполняется метод split, который 
создает список токенов, состоящих из цифр, а затем к каждому токену применяется функция int. 
В результате этого получается список цифр.'''

'''Метод join позволяет объединить iterable строк, используя ту строку, к которой он применен, 
в качестве разделителя.'''
print(', '.join(['Veni', 'Vidi', 'Vici']))

'''Метод join позволяет быстро и коротко выводить списки чисел. Проблема в том, что он умеет 
принимать в качестве параметра только iterable строк. Но с помощью функции map мы можем легко 
получить iterable из списка чисел, применив к каждому элементу функцию str.'''
numList = [1, 2, 3]
print(' '.join(map(str, numList)))


# Полезные методы работы со списками

# Для работы со списками можно использовать циклы for, while

# Для некоторых частных операций существуют уже написанные готовые методы

a = [1, 2, 3, 4, 2, 2, 3]

# Необходимо посчитать количество вхождений в список
print(a.count(10)) # название_списка.count(что_считаем) - O(n)

# a. -> всплывает в среде программирования список возможных методов для работы со списками

a.append('1')
# Метод append позволяет добавить в конец списка какой-то новый элемент
# При этом он изменяет содержимое списка

a.extend([1, 3, 5, 2, 2])
# Добавить к содержимому списка содержимое другого списка
b = [4, 5]
a.extend(b)
print(a)

a = a + b
print(a)

# Результат тот же самый. В чем разница?

# Когда мы пишем итерацию + для двух списков, у нас создается новый объект в памяти,
# в который сначала копируется все содержимое первое списка, а потом - второго списка.
# А ссылка для переменной a начинает показывать на этот объект.

# В большинстве случаев без разницы.
# Кроме случаев, когда передается, например, функция и хотите сделать extend. Тогда extend
# сделать можно, а сложение - нельзя.

# Но есть ситуации, когда это очень сильно отличается по произведительности и потреблению памяти.
# Например, если нужно скреплять огромную последовательность списков в один список.

a.remove(2) # Удалить первое вхождение
print(a)

a.copy()  # Создает и возвращает копию списка
# То же самое, что и взять срез со всеми элементами
# При этом при изменении a b меняться не будет

a.insert(2, 10)  # Позволяет вставить в списоьк какой-то элемент
# Куда и какой

# i - обычно целое число, индекс

# Insert Работает за длину списка, копируя сдвигающиеся элементы

a.pop() # Удаляет последний элемент списка - O(1)
a.pop(3)  # Удаляет укзаанный элемент - O(n) - все элементы явно копируются. переставляются на один


'''К переменным типа список можно применять методы, перечислим некоторые из них:

Методы, не изменяющие список и возвращающие значение:

count(x) - подсчитывает число вхождений значения x в список. Работает за время O(N)

index(x) - находит позицию первого вхождения значения x в список. Работает за время O(N)

index(x, from) - находит позицию первого вхождения значения x в список, начиная с позиции from. 
Работает за время O(N)

Методы, не возвращающие значение, но изменяющие список:

append(x) - добавляет значение x в конец списка

extend(otherList) - добавляет все содержимое списка otherList в конец списка. 
В отличие от операции + изменяет объект к которому применен, а не создает новый

remove(x) - удаляет первое вхождение числа x в список. Работает за время O(N)

insert(index, x) - вставляет число x в список так, что оно оказывается на позиции index. 
Число, стоявшее на позиции index и все числа правее него сдвигаются на один вправо. Работает за время O(N)

reverse() - Разворачивает список (меняет значение по ссылке, а не создает новый список как myList[::-1]). 
Работает за время O(N)

Методы, возвращающие значение и изменяющие список:

pop() - возвращает последний элемент списка и удаляет его

pop(index) - возвращает элемент списка на позиции index и удаляет его. Работает за время O(N)'''


# Обработка списка

# Мы хотим поудалять все нечетные числа, еще и развернуть задом наперед
a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] % 2 != 0:
        a.pop(i) # Удаляем с iой позиции
print(a)

a = list(map(int, input().split()))
# for i in range(len(a)): # После удаления не пересчитывается, поэтому вываливается в ошибку
i = 0
while i < len(a): # Теперь значение будет каждый раз сравниваться с актуальной длиной списка
    if a[i] % 2 != 0:
        a.pop(i) # Удаляем с iой позиции; элементы передвигаются! нужно смотреть на элемент, следующий за удаляемой позицией
    else:
        i += 1
print(*a)

# Функция pop работает за длину списка. Это очень медленно.

# Часто если нужно что-то поудалять из списка, создаем пустой список, и кладем туда элементы.
a = list(map(int, input().split()))
b = []
for now in a:
    if now % 2 == 0:
        b.append(now)
print(b)

# Если у первого алгоритма скорость O(n^2), то у второго - O(n).


'''Рассмотрим такую задачу: необходимо выбрать все нечетные элементы списка myList и удалить их из него.'''

'''Такое решение будет работать неправильно в ситуации, когда в списке есть хоть одно нечетное число. 
Это связано с тем, что объект без названия с типом iterable и значением range(len(numbers)) сгенерируется 
один раз, когда интерпретатор впервые дойдет до этого места и уже никогда не изменится. Если в процессе 
мы выкинем из списка numbers хоть одно значение, то в процессе перебора всех индексов выйдем за пределы 
нашего списка. range, используемый в for, не будет менять свое значение если в процессе работы изменились 
параметры функции range.'''

'''Решение можно переписать с помощью while:'''
numbers = list(map(int, input().split()))
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
    else:
        i += 1
print(' '.join(map(str, numbers)))

'''Такое решение будет работать, но оно не очень эффективно. Каждый раз при удалении элемента нам придется 
совершать количество операций, пропорциональное длине списка. Итоговое количество операций в худшем случае 
будет пропорционально квадарту количества элементов в списке.

В случае, если нет очень строгого ограничения в памяти, в задачах, где нужно удалить часть элементов списка 
гораздо проще создать новый список, в который нужно добавлять только подходящие элементы.'''

numbers = list(map(int, input().split()))
newList = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        newList.append(numbers[i])
print(' '.join(map(str, newList)))

'''Сложность такого решения пропорциональна длине исходного списка, что намного лучше.'''

# Подробнее о сложности сортировки списков: http://pythonz.net/references/named/slozhnost-operatsii-so-spiskami/
