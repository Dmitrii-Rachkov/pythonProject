"""Модули и Пакеты"""

# В Python есть такое понятие как модули и пакеты (библиотеки).
#
# Модуль - это файл, содержащий Python определения и операторы.
# Имя файла - это имя модуля с добавленным суффиксом *.pydoc
#
# Пакет (библиотека) - это набор модулей Python под общим пространством имён.
# На практике пакет создаётся путём размещения нескольких модулей Python в каталоге
# со специальным модулем __init__.py (файл)
#
# Модуль sys предлагает методы, которые позволяют работать с разными элементами среды
# выполнения Python и с его помощью можно взаимодействовать с интерпретатором, используя разные функции.
#
# Импортируют модули или пакеты при помощи слова import, после него пишут название модуля.

import sys

# Текущая версия Python
print(sys.version)

# можно импортировать пакеты и обозвать их новым именем и потом обращаться к ним
import math as m
print(m.cos(50))

# установка пакетов через терминал
# pip3 install numpy
# сайт где можно посмотреть все пакеты
# https://pypi.org

# Можно также в проекте создавать свои папки (пакеты) и файлы (модули) и из них всё импортировать
