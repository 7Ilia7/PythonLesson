a = int(input("Input first value: "))
b = int(input("Input second value: "))
c = str(input("Input action(+,-,*,/): "))
if c == "0":
    print("На ноль делить нельзя")
elif c == "+":
    print("Result: " + str(a + b))
elif c == "-":
    print("Result: " + str(a - b))
elif c == "*":
    print("Result: " + str(a * b))
elif c == "/":
    try:
        result = int(a / b)
    except ZeroDivisionError:
        result = 0
    print("You can not devide by 0")
    print("Result: " + str(result))
else:
    print("Неверный знак операции!")