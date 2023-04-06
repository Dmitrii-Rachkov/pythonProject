var_1 = 10 # глобальная переменная
var_2 = 20 # глобальная переменная

def summ():
    var_1 = 30 # локальная переменная
    var_2 = 40 # локальная переменная
    result = var_1 + var_2
    print(result)

print(var_1, var_2)

summ()

var_3 = 100
var_4 = 70

def jes_plus():
    result = var_3 + var_4
    print(result)

def jes_minus():
    result = var_3 - var_4
    print(result)

jes_plus()
jes_minus()
# в этих двух примерах мы видим что с глобальными переменными мы можем
# выполнять и сложение и вычитание


