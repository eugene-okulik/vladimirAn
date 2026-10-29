i = 348

while True:
    user_input = int(input("Введи цифру: "))
    if user_input == i:
        print("Поздравляю")
        break
    elif user_input != i:
        print("Попробуй снова")
        continue
