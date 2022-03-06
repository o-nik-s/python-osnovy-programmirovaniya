# Выборы Государственной Думы

# Статья 83 закона “О выборах депутатов Государственной Думы Федерального
# Собрания Российской Федерации” определяет следующий алгоритм
# пропорционального распределения мест в парламенте.

# Необходимо распределить 450 мест между партиями, участвовавших в выборах.
# Сначала подсчитывается сумма голосов избирателей, поданных за каждую партию
# и подсчитывается сумма голосов, поданных за все партии. Эта сумма делится
# на 450, получается величина, называемая “первое избирательное частное”
# (смысл первого избирательного частного - это количество голосов избирателей,
# которое необходимо набрать для получения одного места в парламенте). Далее
# каждая партия получает столько мест в парламенте, чему равна целая часть
# от деления числа голосов за данную партию на первое избирательное частное.
# Если после первого раунда распределения мест сумма количества мест, отданных
# партиям, меньше 450, то оставшиеся места передаются по одному партиям,
# в порядке убывания дробной части частного от деления числа голосов за данную
# партию на первое избирательное частное. Если же для двух партий эти дробные
# части равны, то преимущество отдается той партии, которая получила большее
# число голосов.

# На вход программе подается список партий, участвовавших в выборах. Каждая
# строка входного файла содержит название партии (строка, возможно, содержащая
# пробелы), затем, через пробел, количество голосов, полученных данной партией
# – число, не превосходящее 10⁸.
#
# Программа должна вывести названия всех партий и количество голосов
# в парламенте, полученных данной партией. Названия необходимо выводить
# в том же порядке, в котором они шли во входных данных.


n = 450
partyDict = dict()
partyList = list()
voices = 0
inFile = open("input.txt", "r", encoding='utf-8')
for line in inFile:
    party = line.strip()
    count = party.split()[-1]
    party = party[:len(party)-len(count)-1]
    print(party, count)
    partyDict[party] = [partyDict.get(party, 0) + int(count), 0, 0]
    voices += int(count)
    partyList.append(party)
inFile.close()
firstValue = voices // n
print('firstValue', firstValue)
count = 0
restList = list()
for party in partyList:
    if firstValue > 0:
        partyDict[party][1] = partyDict[party][0] // firstValue
        partyDict[party][2] = partyDict[party][0] % firstValue
    count += partyDict[party][1]
    restList.append((party, partyDict[party][1], partyDict[party][2]))
    restList.sort(key=lambda p: (-p[2], -p[1], p[0]))
print(partyDict)
print(restList)
count = n - count
i = 0
while i < count:
    party = restList[i % len(restList)][0]
    partyDict[party][1] = partyDict.get(party, 0)[1] + 1
    i += 1
outFile = open("output.txt", "w", encoding='utf-8')
voices = 0
for party in partyList:
    voices += partyDict[party][1]
    print(party, partyDict[party][1], file=outFile)
outFile.close()
print(partyDict)
print(partyList)
print(voices)
