import os
import csv
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
# collection_ref = firestore.client().collection("item")
db = firestore.client()
collection_ref = db.collection("Cart")  # Specify your collection name

query = collection_ref.where("emailOwner", "==", "mina@qr-catering.eu")
results = query.stream()
fieldnames = None
rows = []

for doc in results:
    data = doc.to_dict()
    if fieldnames is None:
        fieldnames = data.keys()  # Use the keys of the first document as the header
    rows.append(data)

# Write to CSV
csv_file = "mina@qrcateringCart.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
