import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import csv

from openpyxl.workbook import Workbook

# Initialize Firebase Admin using your specified credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Query the Firestore database
collection_ref = db.collection("item")  # Укажите вашу коллекцию
query = collection_ref.where("Visible", "==", True)
docs = query.stream()

# Создаем новый Excel файл
file_path = '../../../static_files/all_items19032025.xlsx'
workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Items"

# Собираем все возможные заголовки
all_keys = set()

# Первый проход: собираем все ключи
document_data = []  # Храним все данные, чтобы обработать их позже
for doc in docs:
    data = doc.to_dict()
    document_data.append(data)
    all_keys.update(data.keys())

# Преобразуем множество ключей в список и записываем заголовки
headers = list(all_keys)
worksheet.append(headers)

# Второй проход: записываем данные, заполняя отсутствующие значения пустыми строками
for data in document_data:
    row_data = [data.get(key, "") for key in headers]  # Если ключ отсутствует, вставляем ""
    worksheet.append(row_data)

# Сохраняем файл
workbook.save(file_path)
print(f"Данные успешно записаны в {file_path}")