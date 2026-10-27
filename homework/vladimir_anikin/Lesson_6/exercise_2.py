numbers = list(range(1, 101))
n_number = []
for number in numbers:
    if number % 5 == 0 and number % 3 == 0:
        n_number.append("FuzzBuzz")
    elif number % 5 == 0:
        n_number.append("Buzz")
    elif number % 3 == 0:
        n_number.append("Fuzz")
    else:
        n_number.append(number)
print(n_number)
