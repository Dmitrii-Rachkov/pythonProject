str_1 = "Hello"
print(str_1)
print(dir(str_1))
# функция 'dir' показывает все возможные действия с переменной 'str_1'
# а функция print соответственно выводит на печать и показывает нам все
# мы можем написать нашу переменную и поставить точку, в подсказках мы увидим возможные операции

str_2 = "world"
print(str_2.upper())
# upper - переводит из нижнего регистра в верхний все буквы в переменной
# если буквы уже в верхнем регистре то ничего не измениться
str_3 = "ExamplE"
print(str_3.upper())

str_4 = "menu"
print(str_4.title())
# Переводит только первый символ в верхний регистр

str_5 = "RAMBO"
print(str_5)
print(str_5.lower())
# lower - позволяет переводить все символы из верхнего регистра в нижний

name = "Ivan"
a = "Hello {}"
result = a.format(name)
print(result)
# {} - эти скобки значат что мы можем поместить в эти скобки какое-то значение
# еще пример ниже
ex = name.format(a)
print(ex)
# ещё пример
b = "Alex {}"
c = "Hello {}"
x = b.format(c)
print(x)

first_name = "Dima"
last_name = "Wick"
f = '{} {}'
res = f.format(first_name, last_name)
print("Меня зовут: " + res)
# сколько скобок фигурных столько и переменных можно поместить в функцию 'format'
# только я не понял почему кавычки одинарные, работает ведь и с двойными

result_new = f'{first_name} {last_name}'
print("Меня зовут: " + result_new)
# f'{} {}' - это называется 'f string нотация' - она аналогична функции 'format' и
# позволяет экономить место


