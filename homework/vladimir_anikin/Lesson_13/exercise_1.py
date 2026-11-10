import os
import datetime


path = os.path.dirname(__file__)
hw_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
hw_file_path = os.path.join(hw_path, "eugene_okulik", "hw_13", "data.txt")
print(hw_file_path)


with open(hw_file_path, "r", encoding="utf-8") as data_file:
    for line in data_file:
        line = line.strip()

        left_part, _ = line.split(" - ", 1)
        number, date_str = left_part.split(". ", 1)
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        if number == "1":
            print(date_obj + datetime.timedelta(days=7))
        elif number == "2":
            print(date_obj.strftime("%A"))
        elif number == "3":
            print((datetime.datetime.now() - date_obj).days)
