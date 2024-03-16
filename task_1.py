import os
import sys
import logging
from collections import namedtuple

# Создаем именованный кортеж для представления элемента директории
DirEntry = namedtuple("DirEntry", ["name", "extension", "is_directory", "parent_directory"])


def list_directory_contents(directory_path):
    try:
        # Проверяем существует ли указанная директория
        if not os.path.exists(directory_path):
            logging.error("Указанная директория не существует.")
            return

        # Получаем содержимое директории
        contents = os.listdir(directory_path)

        # Получаем название родительской директории
        parent_directory = os.path.basename(os.path.abspath(directory_path))

        # Создаем список объектов namedtuple для каждого элемента директории
        dir_entries = []
        for item in contents:
            full_path = os.path.join(directory_path, item)
            is_directory = os.path.isdir(full_path)

            # Если это файл, получаем его имя без расширения и расширение
            if not is_directory:
                filename, file_extension = os.path.splitext(item)
                entry_name = filename
                extension = file_extension
            else:
                entry_name = item
                extension = ""

            # Создаем объект namedtuple для элемента директории
            dir_entry = DirEntry(name=entry_name, extension=extension, is_directory=is_directory,
                                 parent_directory=parent_directory)
            dir_entries.append(dir_entry)

        return dir_entries
    except Exception as e:
        logging.error("Ошибка: %s", e)


if __name__ == "__main__":
    # Конфигурируем логирование
    logging.basicConfig(filename='directory_contents.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')

    # Проверяем, был ли передан путь к директории как аргумент командной строки
    if len(sys.argv) != 2:
        logging.error("Использование: python task_1.py <путь_к_директории>")
    else:
        path_directory = sys.argv[1]
        entries = list_directory_contents(path_directory)
        if entries:
            logging.info("Содержимое директории %s:", path_directory)
            for entry in entries:
                logging.info("Имя: %s", entry.name)
                logging.info("Расширение: %s", entry.extension)
                logging.info("Файл? %s", "Нет" if entry.is_directory else "Да")
                logging.info("Каталог? %s", "Да" if entry.is_directory else "Нет")
                logging.info("Родительский каталог: %s", entry.parent_directory)
                logging.info("")
