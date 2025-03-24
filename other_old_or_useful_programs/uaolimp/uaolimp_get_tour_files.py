import mimetypes
import os
import re

import openpyxl
import requests
from openpyxl import Workbook
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("G:\\FIles\\firebase\\uainternetolimp-41dd1-firebase-adminsdk-i78pu-fd374d92bc.json")
firebase_admin.initialize_app(cred)

# Reference the Firestore collection
db = firestore.client()
collection_ref = db.collection("users")

student_id = "wSnmRKRqOs"  # Замените на ID студента
paralel = "class_example"          # Например, 10A

# Функция для скачивания файла
def download_file(url, save_dir, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        # Определяем MIME-тип и расширение файла
        mime_type, _ = mimetypes.guess_type(file_name)
        # Сохраняем файл
        file_path = os.path.join(save_dir, file_name)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Файл {file_name} успешно сохранен в {save_dir}")
    else:
        print(f"Ошибка при скачивании {url}: {response.status_code}")

# Основная функция
def download_student_tasks(student_id, paralel, task_count=5):
    # Поиск студента в коллекции
    student_ref = collection_ref.where("userId", "==", student_id).get()
    if not student_ref:
        print("Студент не найден")
        return

    student_data = student_ref[0].to_dict()
    save_dir = os.path.join(os.getcwd(), "../downloads")  # Папка для загрузки файлов
    os.makedirs(save_dir, exist_ok=True)

    for task_id in range(1, task_count + 1):
        task_field = f"task_{task_id}"
        file_url = student_data.get(task_field)
        if file_url:
            # Генерация имени файла
            file_name_with_random = os.path.basename(file_url.split('?')[0])
            file_name_cleaned = re.sub(r'_[a-zA-Z0-9]{6}$', '', file_name_with_random)
            _, file_extension = os.path.splitext(file_name_cleaned)
            download_file_name = f"{student_id}_{student_data.get('paralel')}_{task_id}{file_extension}"

            # Скачивание файла
            download_file(file_url, save_dir, download_file_name)
        else:
            print(f"Поле {task_field} не содержит ссылки")

# Запуск функции
download_student_tasks(student_id, paralel)