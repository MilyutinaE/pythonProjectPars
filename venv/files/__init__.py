import os.path

FILES_DIR = os.path.dirname(__file__) # название директории, в которой лежит сам файл __инит__.ру


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)
# возвращает абсолютный путь к заданному файлу путем объединения названия файла и файла, в котором лежит __инит__.ру


TXT_FILE_PATH = get_path(filename="example.txt")
CSV_FILE_PATH = get_path(filename="books.csv")
JSON_FILE_PATH = get_path(filename="users.json")
# константы, которые записываются функцией get_path и передачей в них нужного названия файла
# конструиуется путь к файлу на лету при выполнении скрипта