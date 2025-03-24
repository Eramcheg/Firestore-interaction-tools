import json

import openpyxl
import csv
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../static_files/key5_Terminal.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Получаем все документы из коллекции "ITEMS"
items_ref = db.collection("Product")
docs = items_ref.stream()

items_list = []
for doc in docs:
    item_data = doc.to_dict()
    if len(item_data)!=16:
        print('==================')
        print(len(item_data))
        print(item_data)
        print('==================\n')
    item_data["id"] = doc.id  # Добавляем ID документа
    items_list.append(item_data)

# Сохраняем в JSON
with open("terminalitems.json", "w", encoding="utf-8") as f:
    json.dump(items_list, f, indent=4, ensure_ascii=False)