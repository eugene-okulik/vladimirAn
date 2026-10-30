import sys

sys.set_int_max_str_digits(50000)


def fibonachi():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


number = fibonachi()
wanted_indexes = [5, 200, 1000, 100000]
for i in range(max(wanted_indexes) + 1):
    val = next(number)
    if i in wanted_indexes:
        print(f"{i}-е число Фибоначчи: {val}")
