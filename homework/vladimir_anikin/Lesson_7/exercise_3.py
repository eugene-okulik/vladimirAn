a = "результат операции: 42"
b = "результат операции: 54"
c = "результат работы программы: 209"
d = "результат: 2"

x = 10


def calc(numb):
    number = int(numb.split(":")[-1])
    print(number + x)


for text in [a, b, c, d]:
    calc(text)
