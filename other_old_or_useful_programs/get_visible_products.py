import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import csv

# Initialize Firebase Admin using your specified credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Query the Firestore database
collection_ref = db.collection("item")  # Specify your collection name
query = collection_ref.where("Visible", "==", True)

docs = query.stream()

# Extract 'name' fields and write them to a CSV file
with open('../static_files/all_items06012025.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name'])  # Write CSV header

    for doc in docs:
        data = doc.to_dict()
        name = data.get('name')
        if name:
            writer.writerow([name])

print("CSV file created successfully.")