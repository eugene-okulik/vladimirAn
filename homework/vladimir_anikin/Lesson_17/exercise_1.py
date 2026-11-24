import argparse
import os

parser = argparse.ArgumentParser(description="Анализатор лог-файлов")
parser.add_argument("file", help="Путь к файлу или папке с логами")
parser.add_argument("-t", "--text", required=True, help="Текст для поиска")
parser.add_argument("--full", action="store_true", help="Вывести блок ошибки целиком")
args = parser.parse_args()

# 1. Собираем список файлов
files = []
if os.path.isfile(args.file):
    files.append(args.file)
elif os.path.isdir(args.file):
    for item in os.listdir(args.file):
        full_path = os.path.join(args.file, item)
        if os.path.isfile(full_path):  # Проверяем, что это именно файл, а не подпапка
            files.append(full_path)
else:
    print("Указанный путь не существует.")
    exit()

# 2. Обрабатываем каждый файл
for file_path in files:
    blocks = {}
    current_time = None
    file_name = os.path.basename(file_path)

    with open(file_path, "r", encoding="utf-8", errors="ignore") as log_file:
        for line in log_file:
            # Проверяем начало нового блока (формат даты YYYY-...)
            if len(line) >= 5 and line[:4].isdigit() and line[4] == "-":
                # Берем первые два элемента (дату и время) как ключ
                parts = line.split()
                current_time = f"{parts[0]} {parts[1]}" if len(parts) >= 2 else parts[0]
                blocks[current_time] = [line]
            elif current_time is not None:
                blocks[current_time].append(line)

    # 3. Ищем текст в собранных блоках
    for err_time, lines in blocks.items():
        full_text = "".join(lines)

        if args.text in full_text:
            print(f"\nФайл: {file_name} | Время: {err_time}")

            if args.full:
                print(full_text.strip())
            else:
                words = full_text.split()
                for i, word in enumerate(words):
                    if args.text in word:
                        start = max(0, i - 5)
                        end = i + 6
                        snippet = " ".join(words[start:end])
                        print(f"Фрагмент: ... {snippet} ...")
                        break  # Выводим первое вхождение в блоке (убери break, если нужны все)
            print("-" * 50)
