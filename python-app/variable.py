var_1 = 10 #глобальная переменная
var_2 = 20 #глобальная переменная

def summ():
    var_1 = 30 #локальная переменная
    var_2 = 40 #локальная переменная
    result = var_1 + var_2
    print(result)
print(var_1, var_2)
summ()

var_1 = 100 #глобальная переменная
var_2 = 20 #глобальная переменная

# def summ():
#     result = var_1 + var_2
#     print(result)
# print(var_1, var_2)
# summ()


def summ():

    result = var_1 + var_2
    print(result)

summ()

def sub():

    result = var_1 - var_2
    print(result)

sub()