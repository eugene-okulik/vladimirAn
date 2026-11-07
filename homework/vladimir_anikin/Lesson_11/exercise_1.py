class Book:
    material_page = "материал: бумага"
    text = "кирилица"

    def __init__(self, name, author, page_count, is_reserved=False):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.is_reserved = is_reserved


book1 = Book("Идиот", "Достоевский", 500)
book2 = Book("Преступление и наказание", "Достоевский", 450)
book3 = Book("Братья Карамазовы", "Достоевский", 800)
book4 = Book("Игрок", "Достоевский", 200)
book5 = Book("Бесы", "Достоевский", 600)

book4.is_reserved = True
library = [book1, book2, book3, book4, book5]

for book in library:
    base_info = (
        f"Название: {book.name}, "
        f"Автор: {book.author}, "
        f"страниц: {book.page_count}, "
        f"материал: {book.material_page}"
    )

    if book.is_reserved:
        print(f"{base_info}, зарезервирована")
    else:
        print(base_info)


class School_books(Book):
    def __init__(
        self,
        name,
        author,
        page_count,
        subject_name,
        class_name,
        exercise=False,
        is_reserved=False,
    ):
        super().__init__(name, author, page_count, is_reserved=False)
        self.subject_name = subject_name
        self.class_name = class_name
        self.exercise = exercise


tutorial1 = School_books("Алгебра", "Иванов", 200, "Математика", 9, True)
tutorial2 = School_books("История России", "Петров", 250, "История", 11, False)
tutorial3 = School_books("География", "Сидоров", 180, "География", 7, True)

tutorial1.is_reserved = True
school_library = [tutorial1, tutorial2, tutorial3]
for book in school_library:
    base_info = (
        f"Название: {book.name}, Автор: {book.author}, страниц: {book.page_count}, "
        f"предмет: {book.subject_name}, класс: {book.class_name}, задания: {book.exercise}"
    )

    if book.is_reserved:
        print(f"{base_info}, зарезервирована")
    else:
        print(base_info)
