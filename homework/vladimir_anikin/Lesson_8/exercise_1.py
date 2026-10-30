import random


Salary = int(input("Какая Salary: "))
bonus = random.choice([True, False])
r_bonus = random.randint(100, 5000)
if bonus:
    Salary += r_bonus
print(f"${Salary}")
