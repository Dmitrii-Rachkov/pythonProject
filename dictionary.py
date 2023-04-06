family = ["Alex", "Olga", "Semen", "Nastya", "Alex"]
print(family)
# список [] - квадратные скобки
# список выводит на печать все элементы даже если они одинаковы
# список выдаёт все элементы по порядку


brigada_1 = {"Alex", "Olga", "Semen", "Nastya", "Alex", "alex"}
print(brigada_1)
# множества {} - фигурные скобки
# множества выводятся на печать только с оригинальными единичными объектами
# если регистр у элементов разный, то это считается оригинальным объектом
# элементы в множестве выводятся на печать в случайном порядке

# Когда использовать списки, а когда массивы?
# Если вы имейте большой массив данных и вам необходимо работать с каждым его элементом
# вне зависимости от того повторяется он или нет то используется список
# Если есть большой массив данных и вы хотите отсортировать те элементы которые повторяются
# использовать только оригинальные одиночные элементы, то используйте множества


dream = {"Father": "Alex", "Mother": "Olga", "Brother": "Semen", "Sister": "Nastya"}
print(dream["Mother"], dream["Sister"])
# словарь (ключ:значение)
# у словаря есть два обязательных элемента: ключ, значение
# именно по ключу мы можем получать определенные значения которые нам нужны

for k, v in dream.items():
    print(k, v)
# мы объявляем цикл 'for' и две переменные k - ключ, v - значение
# берём их в нашем словаре 'dream' и подключаем функцию 'items' которая обозначает элементы
# и далее мы говорим чтобы наш цикл 'for' прошёл по всему словарю
# прошёл по всем нашим ключам и значениям и вывел на печать все ключи словаря
# print(v) - выводит все значения
# print(k, v) - выводит и ключи и значения

bob = {"Alex", "Olga", "Semen", "Nastya", "Alex", "alex"}
for b in bob:
    if b == "Olga":
        print(b + " Love")
    else:
        print(b + " Witcher")


