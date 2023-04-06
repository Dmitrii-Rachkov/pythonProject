students = ["Alex", "Daria", "Chappi", "Olga", "Ivano", "Lonaden"]

for f in students:
    print(f)
# создали переменную 'f' которая будет обращаться к каждому элементу из списка
# и выводить на печать элемент
# название переменной 'f' может быть любым

for i in students:
    var = "Electrik " + i
    print(var)
# прибавляем к каждому элементу списка слово и выводим на печать

for a in students:
    if a == "Olga":
        var = "Rambo " + a
        print(var)
# переменная 'var' и функция 'print' видны только условному оператору 'if'
# они не видны циклу 'for'

for b in students[:3]:
    print("Start " + b)
# получаем только 3 первых элемента из нашего списка
# от индекса 0 до 3 не включительно

for e in students[2:]:
    print("Finish " + e)
# получаем последние элементы из списка начиная от индекса 2 до конца списка
# это я так понял

for dia in students[2:4]:
    print("Done " + dia)
# выводим элементы только с 2 по 4 индекс не включительно

for dlina in students:
    print(len(dlina))
# выводим длину каждого элемента из списка с помощью 'len'

