import openpyxl
import csv
import io
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("G:\\FIles\\firebase\\uainternetolimp-41dd1-firebase-adminsdk-i78pu-fd374d92bc.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = firestore.client().collection("tasks")

def upload_tasks_to_firestore():
    # Задаем классы и количество задач
    classes = [9, 10, 11]
    num_tasks = 5

    for class_num in classes:
        for task_num in range(1, num_tasks + 1):
            # Формируем идентификатор задачи, например "9_1"
            task_id = f"{class_num}_{task_num}"

            # Данные задачи, которые будут добавлены в Firestore
            task_data = {
                'max_points': 0,  # Можно задать начальное значение, например, 0 баллов
                'task_id': task_id,
                'class': class_num
            }

            # Добавляем задачу в коллекцию "tasks"
            collection_ref.document(task_id).set(task_data)
            print(f"Задача {task_id} добавлена в Firestore.")

# Вызов функции для загрузки задач
upload_tasks_to_firestore()