num_1 = 10
num_2 = 20
result = num_1 + num_2
print(result)

num_1 = 30
num_2 = 40
result = num_1 + num_2
print(result)
# всё это повторяющиеся действия, а функции позволяют нам упростить код и не писать одно и тоже

def summ():
    print("Hello")

summ()
# итак если мы нажимаем 'enter' в функции то мы как бы продолжаем писать код в функции
# об этом также говорят четыре пробела вначале
# строкой 'summ()' мы вызываем эту функцию

num_3 = 5
num_4 = 6

def summ_1():
    result = num_3 + num_4
    print(result)

summ_1()
# в итоге наш конд тал не сильно короче но мы это исправим дальше

def summ_2(num_5, num_6):
    res = num_5 + num_6
    print(res)


summ_2(4, 5)
summ_2(30, 40)
summ_2(-3, 15)
# таким образом мы экономим место
summ_2("Hello", " Ben")
# эту же функцию можно использовать для сложения строчных типов данных
summ_2(num_6="Hello", num_5=" Ben")
# этой конструкцией в параметрах мы можем сразу задать какой переменной присвоить значение
# тем самым мы определяем порядок переменных в функции


def hi(name="Oleg"):
    print("Privet " + name)
hi()
# можно сразу в функции прописать name="Oleg" - в этом случае всегда
# система будет здороваться с Oleg

surname = "John"
def lem(surname, age):
    print("Privet " + surname + " years of " + age)
lem(surname, "32")


enter = input()
let = input()
def kuk(one, two):
    print("Privet " + one + " years of " + two)

kuk(enter, let)
# также мы можем в функцию закидывать данные с консоли

element = "Mister"
moon = "60"
def roll(one, two):
    res = one + " " + two
    return res

full = roll(element, moon)
print(full)
# можем использовать 'return' для возврата полученного значения в функции,
# далее сохранить значение в переменную 'full' и вывести её на печать
# так мы делаем если хотим в дальнейшем использовать нашу переменную
print(roll(element, moon))
# а здесь мы не используем промежуточных переменных, мы сразу выводим результат

