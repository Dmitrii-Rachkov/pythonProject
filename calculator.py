# Проверяем, что пользователь ввёл целое число
try:
    num_1 = int(input("Введите первое целое число: "))
except ValueError:
    print("Ошибка. Необходимо ввести целое число. Перезапустите программу! ")
    quit()


operation = input("Введите один из арифметических знаков: +, -, *, /")

# Проверяем, что пользователь ввёл арифметический знак
if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("Ошибка. Вы ввели неверный арифметический знак. Перезапустите программу!")
    quit()
else:
    print("Вы ввели: " + operation)

# Проверяем, что пользователь ввёл второе целое число
try:
    num_2 = int(input("Введите второе целое число: "))
except ValueError:
    print("Ошибка. Необходимо ввести целое число. Перезапустите программу! ")
    quit()

# В зависимости от операции делаем арифметические действия
if operation == "+":
    result = num_1 + num_2
    print("Сумма двух чисел: " + str(result))
elif operation == "-":
    result = num_1 - num_2
    print("Разность двух чисел: " + str(result))
elif operation == "*":
    result = num_1 * num_2
    print("Результат умножения: " + str(result))
elif num_2 == 0:
        print("Ошибка. На ноль делить нельзя! ")
        quit()
else:
    result = num_1 / num_2
    print("Результат деления: " + str(result))

