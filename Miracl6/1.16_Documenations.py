"""Добавление документации"""

# Документацию необходимо добавлять не только для описания классов, его атрибутов,
# но и для документирования ваших функций, которые не описаны в каком-либо классе!

# Примеры листинга: https://pythobyte.come/python-docstrings-27502/
# https://peps.python.org/pep-0257/

# Какие есть типы docstring: одностроковые и многостроковые

# Где можно почиать дополнительно о документации по PEP 257 (соглашение о docstrings)
# https://habr.com/ru/post/499358/

# Пример:

"""
    Расчёт и вывод параметров прямоугольника
    
    Attributes
    ----------
    width : int
        ширина прямоугольника
    length : int
        длина прямоугольника
        
    Methods
    -------
    perimeter():
        расчёт периметра прямоугольника
    show_perimeter():
        вывод периметра прямоугольника
"""

# Документация будет доступна через метод:
# print(RectangleNew.__doc__)

# или вот так:
# RectangleNew?