a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение:"))

try:
    result = int(a / b)
except ZeroDivisionError:
    print("На ноль делить нельзя")
    result = 0
print("Результат: " + str(result))

# ZeroDivisionError: division by zero - исключение которое говорит нам о том что делить на '0' нельзя
# ValueError: invalid literal for int() with base 10: 'ф' - исключение говорит нам о неверном типе данных
# нам нужно сделать так чтобы программа продолжила свою работу не смотря на исключение
# конструкция try - except ловит исключения и обрабатывает их как мы захотим и продолжит работу

result_2 = a + b
print(result_2)
# как видите код дальше продолжает работать
