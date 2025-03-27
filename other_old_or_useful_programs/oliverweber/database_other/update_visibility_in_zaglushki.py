import firebase_admin
from firebase_admin import credentials, firestore
import csv

# Initialize Firebase Admin
cred = credentials.Certificate("G:\\Files\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Read names from CSV
names = []
with open('../../../static_files/zaglushki.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        if row:  # Ensure the row is not empty
            names.append(row[0])

# Update documents in Firestore
for name in names:
    # Query for documents with the given name
    query = db.collection("item").where("name", "==", name)
    docs = query.stream()

    for doc in docs:
        # Update the 'Visible' field of each document
        doc.reference.update({"Visible": False})
        print(f"Updated document {doc.id} with name {name} to set Visible=False")

print("Completed updating the Visible field for all matched documents.")
