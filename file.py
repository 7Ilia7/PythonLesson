# var = input("Напиши что-нибудь: ")
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

# а - запись новых данных и помещенние новых  данных в конец списка
# w - запись новых данных , но с удлением старых данных

# var = input("Напиши что-нибудь: ")
# fw = open('doc/file.txt', 'w')
# fw.write(var)
# fw.close()

#Чтение и вывод

fr = open('doc/file.txt', 'r')
text = fr.read()
fr.close()

print(text)


