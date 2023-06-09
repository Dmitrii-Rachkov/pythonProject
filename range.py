# функция 'range' нужна для создания списка содержащего арифметическую прогрессию
# и она может включать в себя только целостные числа как тип данных
# функция 'range' включает в себя следующие параметры:
# старт, стоп, шаг

# range(0, 10, 2)
# первая цифра - то с какой цифра начинается отчет
# вторая цифра - то по какую цифру будет идти отчет
# третья цифра - шаг

r = list(range(10))
print(r)
# 'list()' - обозначает что мы создаём список
# таким образом мы создали список из 10 элементов от 0 до 9
# когда мы пишем 'range(10)' - это значит что 10 это максимальное значение
# по умолчанию шаг = 1 я так понял

s = list(range(0, 10))
print(s)
# получаем тотже результат, мы показываем что отсчет от 0 до 10

a = list(range(5, 10))
print(a)
# список с элементами от 5 до 10 не включительно

x = list(range(0, 13, 3))
print(x)
# создаем список с шагом 3

for f in range(10):
    print(f)
# проходим по нашему созданному списку range и выводим каждый элемент на печать
