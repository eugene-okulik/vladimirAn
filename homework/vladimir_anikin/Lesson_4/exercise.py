my_dict = {
    "tuple": ("zero", 1, 2, 3, 4),
    "list": ["text", False, 17, 24, "Petr1"],
    "dict": {
        "one": "value",
        "two": "value2",
        "three": "3",
        "asd": "who",
        "qwerty": "klaviotura",
    },
    "set": {"text", False, 2.42, 3, 7},
}


print(my_dict["tuple"][-1])
my_dict["list"].append(34)
my_dict["list"].pop(1)
my_dict["dict"][("i am a tuple",)] = "78"
del my_dict["dict"]["one"]
my_dict["set"].add("NEW")
my_dict["set"].remove(7)
print(my_dict)
