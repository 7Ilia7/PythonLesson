#список
famile_1 = ["alex", "ilia", "semen", "tana", "alex"]
print(famile_1)

#множества
famile_2 = {"alex", "ilia", "semen", "tana", "alex"} #множества пишутся в фигурных {}
print(famile_2) #когда мы выводим множество выводиться только уникальные обьекты(еденичные)

#словарь (ключ:значение)
famile_3 = {"Papa":"Andrei", "Mama":"Tanya", "Son1":"ilia", "Son2":"Daniil"}
# print(famile_3["Papa"])
for k, v in famile_3.items():
    print(k + " - " + v)