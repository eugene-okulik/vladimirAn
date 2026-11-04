def finished(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("finished")

    return wrapper


@finished
def simple1():
    print("simple1")


simple1()

# Для запуска 18-22 строку нужно раскоментить, а 11-15 закоментить
# def example(text):
#     print(text)


# example("print me")
