"""ЦИКЛЫ"""

# В Python есть две команды для использования цикла:
# while - пока условие выполняется, то цикл также выполняется
# for

# пока 'count' меньше 'n' выполняй
count = 0
n = 5

while count < n:
    count += 1
    print(count)

# Пока число меньше или равно 100

cou = 0
num = 100

while cou <= num:
    # если остаток при делении на 2 равен 2
    if cou % 10 == 2:
        cou += 2
    cou += 1

print(cou)

# Цикл for выполняется вот так:
for i in [2, 4, 5]:
    print(i)

# for - оператор начала цикла
# i - переменная текущего элемента итерации
# [2, 4, 5] - последовательность по которой мы итерируемся
# print(i) - код который мы хотим выполнить с каждым элементом

"""RANGE"""

# В качестве множества значений для перебора в for мы можем передавать списки,
# одномерные массивы, или как в примере функцию range()

# Функция range() может также принимать не один, а три параметра.
# Вызов range(a, b, c)
# a - начальное значение
# b - конечное значение не включительно
# c - шаг ( по умолчанию 1)
# если a >= b - то цикл не будет выполнен

for f in range(1, 5):
    print(str(f) + " RANGE")

for k in range(1, 5, 2):
    print(str(k) + " Step 2")

# Выполнить 9 раз
# Мы подаём в функцию range одно число и он понимает что нам нужно от 0 до 9 не включительно
ex_count = 0
ex_n = 9

for s in range(ex_n):
    print(str(s) + " 9 Raz")

# Можно range перевести в список
spisok = list(range(1, 5, 2))
print(f"Список в range {spisok}")

# Оператор 'break' досрочно прерывает цикл
print("Пример с break:")
lst =[]

for i in range(1, 10):
    print(f"i = {i}")
    if 2 < i < 5:
        print(f"break and i = {i}\n")
        break
    else:
        print(f"append and i = {i}\n")
        lst.append(i)
print(lst)

# Оператор 'break' прерывает только тот цикл в котором находится (блок кода)
print("Двойной цикл break")
spi_1 = []
spi_2 = []

for i in range(3, 5):
    for j in range(1, 10):
        print(f"{i = }, {j = }\n")
        if j > 5:
            print(f"append and {i = }, {j = }")
            spi_1.append(i)
        break
    spi_2.append(i)

print(spi_1)
print(spi_2)

"""CONTINUE"""

# При этом операторе при попадании на условие он продолжает выполнять код
print("Continue пример")
pro =[]

for i in range(1, 5):
    print(f"i = {i}")
    if 2 < i < 4:
        print(f"continue and i = {i}\n")
        continue
    else:
        print(f"append and i = {i}\n")
        pro.append(i)
print(pro)




