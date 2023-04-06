fw = open('doc/file.txt', 'a')
fw.write("Hello world\n")
fw.close()
# таким образом мы открываем файл, (если файла нет то создаем его)
# выполняет действие (mode) 'a' - запись новых данных и перемещение их в конец документа
# записываем в файл Hello world
# закрываем файл

garage = open("doc/garage.txt", "a")
car = input("Please write model of car")
garage.write(car + "\n")
garage.close()
# это просто ещё один пример


remove = open('doc/delete.txt', 'w')
remove.write("Lexa\n")
remove.close()
# действие (mode) 'w' - запись новых данных с удалением старых

read = open("doc/garage.txt", 'r')
# действие (mode) 'r' - чтение данных из файла
text = read.read()
read.close()
print(text)


