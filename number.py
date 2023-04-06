print("Sum")
num_1 = 5
num_2 = 10
result_1 = (num_1 + num_2)
print(result_1 + 1)

print("\nMinus")
num_3 = 5
num_4 = 10
result_2 = (num_3 - num_4)
print(result_2 - 2)

print("\nMultiplication")
num_5 = 5
num_6 = 10
result_3 = (num_5 * num_6)
print(result_3 * 3)

print("\nExponentiation_1")
num_9 = 2
print(num_9 ** 5)
# ** - это значит возвести в степень

print("\nExponentiation_2")
num_12 = 2 ** 5
print(num_12)

print("\nDivision with float")
num_13 = 50
num_14 = 8
result_4 = num_13 / num_14
print(result_4)

print("\nDivision without float_1")
num_15 = 50
num_16 = 8
result_5 = num_15 / num_16
print(int(result_5))

print("\nDivision without float_2")
num_17 = 50
num_18 = 8
result_6 = num_17 // num_18
print(result_6)
# // - позволяет отбросить данные после точки и вывести только целое число

print("\nRemainder of the division")
num_19 = 50
num_20 = 8
result_7 = num_19 % num_20
print(result_7)
# % - остаток от деления в нашем случае 8*6=48, 50-48=2

print("\nBoolean True")
num_21 = 5
num_22 = 5
print(num_21 == num_22)

print("\nBoolean False")
num_21 = 8
num_22 = 5
print(num_21 == num_22)

print("\nMore")
num_21 = 8
num_22 = 5
print(num_21 > num_22)

print("\nLess")
num_23 = 8
num_24 = 5
print(num_23 < num_24)

print("\nMore or equal")
num_25 = 8
num_26 = 8
print(num_25 >= num_26)

print("\nLess or equal")
num_27 = 8
num_28 = 8
print(num_27 <= num_28)

print("\nRounding")
num_29 = 10
num_30 = 3
result_8 = num_29 / num_30
print(result_8)
print(round(10/3, 4))
# print(round(10/3, 4)) - эта конструкция позволяет округлить результат до 4 знаков после запятой

print("\nFloat_1")
num_31 = float(10.5)
print(num_31)
# преобразовали целое число в float и вывели его на печать
# мы указываем float чтобы проводить операции с другими типами данных
# и выводить на печать результат с плавающей точкой

print("\nFloat_2")
num_32 = float(10.5)
num_32 = 5.5
print(num_32)

print("\nFloat or int_1")
num_33 = float(10.5)
num_34 = 10
result_9 = num_33 + num_34
print(result_9)
print(int(result_9))

print("\nFloat or int_2")
num_35 = float(10.5)
num_36 = 10
result_10 = int(num_35 + num_36)
print(result_10)
