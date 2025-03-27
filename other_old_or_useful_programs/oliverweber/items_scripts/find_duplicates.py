import openpyxl
import csv
import io
import firebase_admin
from firebase_admin import credentials, firestore
import ftplib
import datetime

cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

items_ref = db.collection('item')

# Fetch documents
docs = items_ref.stream()

# Dictionary to count names
name_count = {}

# Count each name
for doc in docs:
    name = doc.to_dict().get('name', None)
    visible = doc.to_dict().get('Visible', False)
    if visible:
        if name :
            if name in name_count:
                name_count[name] += 1
            else:
                name_count[name] = 1

# Find duplicates
duplicates = [name for name, count in name_count.items() if count > 1]

# Print duplicate names
print("Duplicate names:", duplicates)