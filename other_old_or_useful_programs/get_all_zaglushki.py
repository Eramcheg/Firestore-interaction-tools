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
query = collection_ref.where("Visible", "==", True).where("`image-url`", "==", "https://firebasestorage.googleapis.com/v0/b/flutterapp-fd5c3.appspot.com/o/wall%2Fno_image.jpg?alt=media&token=22a7b907-01f6-45b6-8fb1-f1f884ab21d4")


# Fetch the documents
docs = query.stream()

# Prepare to write to a CSV file
with open('../static_files/zaglushki.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name'])  # Writing the header of the CSV file

    # Iterate over the query results and write to the CSV file
    for doc in docs:
        doc_data = doc.to_dict()
        writer.writerow([doc_data.get('name')])  # Extract the 'name' field and write it

print("Data has been written to 'zaglushki.csv'")
