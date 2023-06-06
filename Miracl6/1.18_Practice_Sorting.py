# Сортируем список по возрастанию методом 'sorted()', который вернёт
# новый отсортированный список

list_1 = [5, 2, 3, 1, 4]
sor = sorted(list_1)
print(f'Метод sorted() для int \n{sor}')

str_list = ['x', 'm', 'a', 'b']
str_s = sorted(str_list)
print(f'Метод sorted() для str \n{str_s}')

# Сортируем список методом 'sort()', который изменяет исходный список

list_2 = [5, 2, 3, 1, 4]
list_2.sort()
print(f'Метод sort() для int \n{list_2}')

str_sort = ['o', 'y', 'a', 't']
str_sort.sort()
print(f'Метод sort() для str \n{str_sort}')

# Сортируем словарь методом 'sorted()'

dict_1 = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
dict_sorted = sorted(dict_1)
print(f'Метод sorted() для dict ключи \n{dict_sorted}')
a = sorted(dict.values(dict_1))
print(f'Сортировкa по значениям \n{a}')

# Вернется список отсортированных ключей словаря

d1 = {2: 'red', 1: 'green', 3: 'blue'}
print(f'Сортировка ключей \n{sorted(d1)}')

# Вернется список отсортированных значений словаря

print(f'Сортировка значений словаря \n{sorted(d1.values())}')

# Вернется список кортежей (ключ, значение), отсортированный по ключам

print(f'Сортировка ключей и значений \n{sorted(d1.items())}')

# Сортируем список по длине с помощью 'key=len'

names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
names.sort(key=len)
print(f'Сортировка по длине элемента \n{names}')

# Аргумент 'reverse' может иметь логическое значение: True или False
# Например reverse=True укажет компьютеру отсортировать список в обратном алфавитном порядке

names_2 = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
names_2.sort(reverse=True)
print(f'Сортировка в обратном алфавитном порядке \n{names_2}')

# Сортировка словаря на основе функции len
l1 = {'carrot': 'vegetable', 'red': 'color', 'apple': 'fruit'}

# Возвращает список ключей, отсортированных по функции len
print(sorted(l1, key=len))
# Вывод: ['red', 'apple', 'carrot']

# Возвращает список значений, отсортированных на основе функции len
print(sorted(l1.values(), key=len))
# Вывод: ['fruit', 'color', 'vegetable']

# Сортировка списка на основе функции len
l1 = ['blue', 'green', 'red', 'orange']
print(sorted(l1, key=len))
# Вывод: ['red', 'blue', 'green', 'orange']

# Разбивает строку и сортирует после применения str.lower ко всем элементам
s1 = "Hello How are you"
print(sorted(s1.split(), key=str.lower))
# Вывод: ['are', 'Hello', 'How', 'you']

# Пользовательские функции для сортировки

# напишем функцию для получения второго элемента
def sort_key(e):
    return e[1]

l1 = [(1, 2, 3), (2, 1, 3), (11, 4, 2), (9, 1, 3)]
# По умолчанию сортировка выполняется по первому элементу
print(sorted(l1))
# Вывод: [(1, 2, 3), (2, 1, 3), (9, 1, 3), (11, 4, 2)]

# Сортировка по второму элементу с помощью функции sort_key
print(sorted(l1, key=sort_key))
# Вывод: [(2, 1, 3), (9, 1, 3), (1, 2, 3), (11, 4, 2)]

# operator — это встроенный модуль, включающий много операторов.
# itemgetter(n) создает функцию, которая принимает итерируемый объект (список, кортеж, множество)
# и возвращает n-элемент из него.

# сортировка списка кортежей по второму элементу в каждом из них.
# itemgetter() возвращает функцию, которая получает третий элемент в кортеже.
# По умолчанию если key не указать, то сортировка будет выполнена по первому элементу кортежа.

from operator import itemgetter

l1 = [(1, 2, 3), (3, 1, 1), (8, 5, 3), (3, 4, 2)]

# Сортировка по второму элементу в кортеже
print(sorted(l1, key=itemgetter(2)))
# Вывод: [(3, 1, 1), (1, 2, 3), (3, 4, 2), (8, 5, 3)]

# Создание списка словарей
d1 = [{'name': 'Paul', 'age': 30},
         {'name': 'Alex', 'age': 7},
         {'name': 'Eva', 'age': 3}]

# Сортировка по key(age) в словаре
print(sorted(d1, key=itemgetter('age')))
# Вывод: [{'name': 'Eva', 'age': 3}, {'name': 'Alex', 'age': 7}, {'name': 'Paul', 'age': 30}]

# Многоуровневая сортировка
# сортировка значений словаря будет выполнена по второму элементу.
# Если же некоторые из них будут равны, то сортировка пройдет по третьему элементу.
d = {'a': [1, 2, 9], 'b': [3, 2, 5], 'c': [1, 1, 2]}

# Сортировка по второму, затем по третьему элементу
print(sorted(d.values(), key=itemgetter(1, 2)))
# Вывод: [[1, 1, 2], [3, 2, 5], [1, 2, 9]]

ex = []
n = 10

# Число фибоначи
def iterativeFib(n):

    a, b = 0, 1
    fib = []

    for i in range(n):
        a, b = b, a + b
        fib.append(a)

    return fib

el = iterativeFib(10)
print(el)

# Строка в обратном порядке
idn = "Hello mister pipa"
res = sorted(idn.split(), reverse=True)
otvet = " ".join(res)
print(otvet)








