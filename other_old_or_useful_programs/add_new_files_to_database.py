import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import csv

cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("item")
file_path = '..\\product_wrapper\\output_file3.csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';',
                            fieldnames=['number', 'name', 'quantity', 'description', 'price', 'image_url1',
                                        'image_url2', 'material', 'plating', 'stone', 'size'])
    next(reader)  # Skip header row if your CSV contains headers
    for row in reader:
        print(row)
        # Convert some fields from string to appropriate types
        row['quantity'] = int(row['quantity'])
        row['price'] = round(float(row['price'].replace(',', '.')),
                             2)  # Convert price to float, replacing comma with dot

        # Remove the 'number' field
        del row['number']

        # Remove the 'size' field only if it equals 'no'
        if row['size'] == 'no':
            del row['size']
        if 'image_url1' in row:
            row['image_url'] = row.pop('image_url1')
        if 'image_url2' in row:
            row['image-url'] = row.pop('image_url2')
        # Check if a document with the same name exists
        existing_docs = collection_ref.where('name', '==', row['name']).get()

        # If exists, delete each found document
        for doc in existing_docs:
            doc.reference.delete()

        # Add document to Firestore
        collection_ref.add(row)

print("Operation completed. Documents were either added or updated in Firestore.")