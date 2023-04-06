"""ИСКЛЮЧЕНИЯЪ"""

# Свои типы исключений
# https://habr.com/ru/company/piter/blog/537642/

# Исключения (exeptions) - ущё один тип данных в python.
# Исключения необходимы для того, чтобы сообщать программисту об ошибках.

# Простейший пример исключения это деление на 0:
# print(100 / 0)

# Разберём сообщение об ошибке поподробней:
# Интерпретатор сообщает нам, что поймал ошибку и напечатал информацию Traceback (most recent call last):
# Далее имя файла (File**). Строка в файле line 10
# Выражение и номер строки в котором произошла ошибка print(100 / 0)
# Название исключения (ZeroDivisionError) и краткое описание исключения (division by zero)

# Наиболее частые исключения:
# ImportError - импортирование не удалось
# IndexError - индекс не входит в диапазон элементов списка
# NameError - попытка использовать несуществующую переменную
# SyntaxError - ошибка разбора кода
# TypeError - в функционал передано значение несовместимого кода
# ValueError - в функцию передано значение совместимого типа, но с некорретным значением

# В Python есть целая иерархия исключений
# https://tatyderb.gitbooks.io/python-express-course/content/chapter_exception/3_tree.html

# Для обработки исключений следует использовать конструкцию try-except
try:
    num = 100 / 0
except ZeroDivisionError:
    num = 0

print(num)

# Ещё пример:
try:
    num = 100
    print(num + " hello")
    print(num / 2)
except ZeroDivisionError:
    print("Division by zero")
except (ValueError, TypeError):
    print("Error occurred")

# Если использовать except без исключений, то он будет- перехватывать все ошибки, данное выражение
# следует использовать с осторожностью, так как может перехватить скрытые ошибки.

# Помимо того что мы можем отлавливать ошибку мы ещё можем и выводить нужный нам текст:
try:
    num = "Hello"
    print(num / 0)
except TypeError as ex:
    print(f'Error message: {ex}')

# Ещё пример
try:
    num = "Hello"
    print(num / 0)
except Exception as ex:
    print(f'Error message: {ex}')

# Если вам необходимо, чтобы вне зависимости от того, возникли ошибки или нет, некоторый фрагмент
# кода выполнялся, то используйте конструкцию finally
# Он располагается в нижней части конструкции try-except.
# Finally выполняется всегда после блока try, и, если возможно, после блока except
try:
    print("first")
    print(100 / 0)
except Exception as ex:
    print(f"Error message: {ex}")
finally:
    print("Hello world")


