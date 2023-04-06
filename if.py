age = 26

if age == 25:
    print("Adult man")
elif age > 25:
    print("Old")
else:
    print("Young")

name = "John"

if age == 25 and name == "John":
    print("You my hero")
elif age > 25 or age < 25 and name == "John":
    print("We are mistake")
else:
    print("Where is John?")


surname = "Wick"

if "c" in surname == "Wick":
    print("My name is Mr. Wick")
else:
    print("I'm Rambo")
# если буква 'i' будет в значении переменной 'surname' то выполнить первое условие
# также здесь есть чувствительность к регистру и языку

pin = 1234
print("What is your pin?")
user_pin = int(input())

if pin == user_pin:
    print("Get many")
else:
    print("Error pin code. You have two choose")
    user_pin = int(input())

    if pin == user_pin:
        print("Get many")
    else:
        print("Error pin code. You have one choose")
        user_pin = int(input())

        if pin == user_pin:
            print("Get many")
        else:
            print("You card is lock")
# пример работы банкомата

