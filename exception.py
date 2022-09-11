a = int(input("Vvedite pervoe znacheniye: "))
b = int(input("Vvedite vtoroe znacheniye: "))

try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print("Na 0 delitb nelza")
print("rezultat: " + str(result))

result_2 = a + b
print(result_2)

#ZeroDivisionError