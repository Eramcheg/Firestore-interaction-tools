import os


def remove_duplicate_files(folder1, folder2):
    """
    Удаляет файлы из folder2, если их имена совпадают с файлами из folder1.

    :param folder1: Путь к первой папке.
    :param folder2: Путь ко второй папке.
    """
    # Получаем список файлов в первой папке
    files_in_folder1 = set(os.listdir(folder1))

    # Проверяем файлы во второй папке
    for file_name in os.listdir(folder2):
        file_path = os.path.join(folder2, file_name)

        # Если файл из второй папки есть в первой, удаляем его
        if file_name in files_in_folder1 and os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Удален файл: {file_path}")


# Укажите пути к папкам
folder1 = "C:\\Users\\eramc\\Downloads\\Telegram Desktop\\Pictures Coins\\Pictures Coins"
folder2 = "C:\\Users\\eramc\\Downloads\\Telegram Desktop\\Corrected Bilder\\Corrected Bilder"

# Вызов функции
remove_duplicate_files(folder1, folder2)
