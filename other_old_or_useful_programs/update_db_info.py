import openpyxl
import csv
import io
import firebase_admin
from firebase_admin import credentials, firestore
import ftplib
import datetime
# Initialize Firebase Admin with your service account credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Reference the collection where you want to update the document
collection_ref = firestore.client().collection("item")

# Load Excel workbook
xlsx_file_path = "C:/Users/eramc/Downloads/new website testing(1).xlsx"
workbook = openpyxl.load_workbook(xlsx_file_path)
sheet = workbook.active

updates = []
names_from_excel = set()
for row in sheet.iter_rows(min_row=2, values_only=True):
    name, plating, size, stone, category, product_name, material = row[1], row[4], row[4], row[8], row[6], row[7], row[2]
    updates.append({
        'name': name,
        'plating': plating if plating else 'Rhodium',
        # 'size': size if size else "Default",
        'stone': str(stone) if stone else 'Default',
        'material': material if material else 'Brass'
        # 'product_name':product_name
    })
    names_from_excel.add(name)


batch = db.batch()
collection_ref = db.collection('item')


for data in updates:
    doc_ref = collection_ref.where('name', '==', data['name']).get()
    if doc_ref:

        for doc in doc_ref:
            # if(data["size"] != "Default"):
                batch.update(doc.reference, {
                    'plating': data['plating'],
                    # 'size': data['size'],
                    'stone': data['stone'],
                    'material': data['material'],
                    # 'product_name': data['product_name']
                })
    else:
        print(f"Document with name {data['name']} not found")

batch.commit()

# all_docs = collection_ref.stream()
# unmodified_names = [doc.to_dict()['name'] for doc in all_docs if doc.to_dict()['name'] not in names_from_excel]
#
# # Generate CSV
# with open('unmodified_names.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name'])
#     for name in unmodified_names:
#         writer.writerow([name])
#
# print("CSV of unmodified documents created.")
