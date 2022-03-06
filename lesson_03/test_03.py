# Методы rfind, replace и count

s = 'abcd abcf abd'

# rfind - поиск первого вхождения справа налево
print(s.rfind('abc'))
# У rfind так же есть параметры

# replace заменяет одну подстроку на другую подстроку
print(s.replace('abc', '1234'))
# Не изменяет исходную строку, но возвращает новый объект с заменами
# Третий параметр означает, сколько первых левых вхождений заменить
print(s.replace('abc', '1234', 1))
# У replace нет параметров, с какого по какое вырезать, но можно сделать срез строки,
# внутри сделать replace, а затем вклеить обратно вместе с левым и правым хвостом.

a = 'aaaaaa'
# Мы хотим 2 буквы a заменить на 1 букву a
print(a.replace('aa','a'))
# Замена выполняется только для непересекающихся строк.

# Если хотим заменить все
s = a
while s.find('aa') != -1:
    s = s.replace('aa','a',1)
print(s)

# count позволяет подсчитать количество вхождений подстроки в строку
s = 'abcdefabc'
print(s.count('abc'))
print(s.count('a'))  # Количество вхождений одной буквы
print(s.count('abcd'))
print(s.count('abac'))  # Если строка вообще не входит, то получаем ноль

s = 'aaaaaa'
print(s.count('aa'))
# count проверяет вхождения не пересекающихся подстрок
# Параметр end - не включителен
print(s.count('aa',1))
