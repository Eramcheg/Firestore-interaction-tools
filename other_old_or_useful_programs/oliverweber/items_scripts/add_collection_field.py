import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import csv
import openpyxl
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("item")

xlsx_file_path = "../../../static_files/Coins and Monograms.xlsx"

wb = openpyxl.load_workbook(xlsx_file_path)
sheet = wb.active

# Чтение данных из колонки A
names = [cell.value for cell in sheet['A'] if cell.value]

# Обновление документов в Firestore
for name in names:
    query = db.collection("item").where("name", "==", name)
    docs = query.get()

    if docs:
        for doc in docs:
            doc.reference.update({"collection": "Coins_And_Monograms"})
            print(f"Updated document: {doc.id}")
    else:
        print(f"Document not found with name: {name}")

print("Update completed.")