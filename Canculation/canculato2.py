a = float(input("Выводите первое число : "))
b = str(input("Введите, какие математические действия будут выполнены + - * / : "))
c = float(input("Выводите второе число : "))
if b == "+":
    print("Результат: " + str(a + c))
elif b == "-":
    print("Результат: " + str(a - c))
elif b == "*":
    print("Результат: " + str(a * c))
elif b == "/":
    try:
        result = int(a / c)
    except ZeroDivisionError:
        result = 0
    print("Вы не можете разделить на 0")
    print("Результат: " + str(result))