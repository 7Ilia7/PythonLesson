pin = 2525
print("Ведите пожаллуйста ваш Pin-код")
user_pin = int(input())

if pin == user_pin:
    print("Какую сумму вы хотите снять?")
else:
    print("Ошибка, введите верный Pin-код, у вас осталось 2 попытки")
    user_pin = int(input())
    if pin == user_pin:
        print("Какую сумму вы хотите снять?")
    else:
        print("Ошибка, введите верный Pin-код, у вас осталось 1 попытка")
        user_pin = int(input())
        if pin == user_pin:
            print("Какую сумму вы хотите снять?")
        else:
            print("Ваша карта заблокирована, пожалуйста обратитесь в банк")
