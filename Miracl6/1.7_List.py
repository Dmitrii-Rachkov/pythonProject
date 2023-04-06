"""СПИСОК"""

# Для создания используем квадратные скобки []

data = ["string", 8.5, 9, 10, False, True]
print(data, type(data))

# можно переводить другие структуры данных в список:
data_2 = list({"string", 8.5, 9, 10})
print(data_2, type(data_2))

# Определяем длину списка:
print(len(data))

# Нумерация элементов списка начинается с нуля (индексы)
print(data[1])
# Так мы вывели элемент под индексом 1

# Посмотреть элементы с 1 по 3 индекс можно с помощью слайсов:
# data[start:stop:step]
# start - индекс первого элемента
# stop - индекс последнего элемента не включается в список
# step - определяем шаг с которым нужно выводить элементы, по умолчанию шаг = 1
print(data[1:3])

# Вывести список без последнего элемента:
print(data[:-1])

# Вывести только последний элемент:
print(data[-1:])

# Перевернуть список
print(data[::-1])

# Изменить значение элемента с индексом '0'
data[0] = 2
print(data)

# Добавить элемент в конец списка
data.append("bar")
print(data)

# Удалить элемент по индексу '1'
data.pop(1)
print(data)

# Удалить элемент с конца списка
data.pop()
print(data)

# Удалить элемент по значению объекта (удалим элемент с значением '2')
data.remove(2)
print(data)
# Если значение не найдено, то будет ошибка
