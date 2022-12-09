from random import randint, choice

k = int(input("Введите степень многочлена "))
res = f"{randint(1, 100)}*x**{k}"
for i in range(k - 1, 0, -1):
    number = randint(0, 100)
    if number != 0:
        if i == 1:
            res = res + choice(["+", "-"]) + f"{number}*x"
        else:
            res = res + choice(["+", "-"]) + f"{number}*x**{i}"

else:
    number = randint(0, 100)
    if number != 0:
        res = res + choice(["+", "-"]) + f"{number}"

with open("file.txt", "w") as f:
    f.write(res)