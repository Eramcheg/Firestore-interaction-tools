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
names2 = [
    "61322", "61324G", "62290", "62292G", "61320G", "61323G", "61321", "61321G", "61320", "62291G", "62289", "62289G",
    "12491G", "12493G", "12492G", "23214G", "23215G", "23216G", "12490G", "23213G", "41229S", "41229M","41229L", "41229XL", "41230S", "41230L", "41230M", "41230XL",
    "32432G", "12482G", "23205G", "32431", "23204", "12484", "23207", "23048", "12481",
    "12483G", "32433G", "23208G", "23206G", "12485G",
    "12489", "12488", "12487", "23212", "23211", "23210", "12486G", "12486", "23209G", "23209",
    "12157 L169I", "12157 L167I", "12157 L168I", "12157 L163I", "22916 L169I", "22916 L167I", "22916 L168I", "22916 L163I", "11522 971S", "11522 214", "22388 971S", "22388 214",
    "11523G 971S", "11523 1405", "11523 1201", "11523G 1002", "22389G 971S", "22389 1405", "22389 1201", "22389G 1002", "12052R 263", "12052R 238", "12052R 277", "22851R 263", "22851R 238", "22851R 277",
    "21009 L110D", "21009 1405", "21009 L134I", "21009 L107D", "21009 L169I", "21009 L142D", "21009 L167I", "21009 L163I", "21009 L168I", "21009 1201", "21009 L137I", "21009 L161I", "63322L BLU", "63322S BLU", "63322M BLU", "63322XL BLU"
]
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