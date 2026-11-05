# def repeat_me(func):

#     def wrapper(*args, **kwargs):
#         count = kwargs.pop("count", 1)
#         for _ in range(count):
#             func(*args, **kwargs)

#     return wrapper


# @repeat_me
# def example(text):
#     print(text)


# example("print me", count=7)


def repeat_me(count=1):  # 1. Сюда теперь прилетает count
    def actual_decorator(func):  # 2. А сюда прилетает сама функция
        def wrapper(*args, **kwargs):  # 3. А это наша обертка для запуска
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return actual_decorator


@repeat_me(count=3)
def example(text):
    print(text)


example("print me")
