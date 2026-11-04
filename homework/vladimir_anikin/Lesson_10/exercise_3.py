def znak(func):
    def wrapper(*args, **kwargs):
        args_list = list(args)

        first = args_list[0]
        second = args_list[1]

        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif first < second:
            operation = "/"
        kwargs["operation"] = operation
        return func(*args_list, **kwargs)

    return wrapper


first = int(input("Введи первую цифру: "))
second = int(input("Введи вторую цифру: "))


@znak
def calc(first, second, operation=None):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


result = calc(first, second)
print("Результат операции:", result)
