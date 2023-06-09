import modul_1

modul_1.some()
# мы импортировали modul_1 в наш файл и теперь мы можем пользоваться функцией 'some'
# если в modul_1 мы переименуем функцию 'some' то система в файле 'start' не сможет её найти
# таким образом мы поработали с самописным модулем modul_1

# import math - это стандартная библиотека python

import math

print(math.pi)
# math - стандартная математическая библиотека python (константы, действия, и т.д.)

import random

r = random.randrange(0, 10, 1)
print(r)
# библиотека 'random' - стандартная для python позволяет получать различные случайные значения

user = "User"
print(user + str(r))

user_random = user + str(r)
print(user_random)

# когда мы импортируем какой-либо самописный модуль и используем его в коде, то после запуска кода
# система ищет модуль в проекте и найдя его использует в коде
# если не находит, она начинает искать модуль с соответствующим названием
# среди стандартных библиотек python
# если система находит модуль в стандартных библиотеках то она использует его в коде
# если не находит - выдаёт ошибку

# когда мы импортируем стандартную библиотеку, то система сначала проверяет есть ли в нашем проекте
# самописный модуль с таким названием и не найдя их, система ищет стандартные библиотеки с таким именем
# в которых она находит или не находит модуль с заданным именем
# и исполняет код или выдаёт ошибку

from mod import some

some.sub(10, 2)
some.sum(10, 2)

