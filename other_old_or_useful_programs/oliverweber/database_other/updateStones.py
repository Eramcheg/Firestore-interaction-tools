import openpyxl
import firebase_admin
from firebase_admin import credentials, firestore
import time
# Initialize Firebase Admin with your service account credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Reference the collection where you want to update the document
collection_ref = firestore.client().collection("item")

# Load the Excel file
xlsx_file_path = "../../../static_files/List with crystals info.xlsx"
workbook = openpyxl.load_workbook(xlsx_file_path)
sheet = workbook['new website testing']

# Iterate through the rows in the Excel sheet
batch_size = 500  # Number of updates to process in one batch
delay_seconds = 5  # Delay between batches in seconds

updates = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    if len(row) < 3 or not row[2]:
        continue  # Skip rows that don't have at least 3 columns or if the third column is empty

    document_name = row[1]  # The second column value
    new_stone_value = row[2]  # The third column value

    # Store the updates
    updates.append((document_name, new_stone_value))

# Process updates in batches
for i in range(0, len(updates), batch_size):
    batch = firestore.client().batch()
    for document_name, new_stone_value in updates[i:i + batch_size]:
        # Query the Firestore collection to find the document by name
        query = collection_ref.where('name', '==', document_name).stream()
        for doc in query:
            doc_ref = collection_ref.document(doc.id)
            batch.update(doc_ref, {"stone": str(new_stone_value)})

    batch.commit()
    print(f"Batch {i // batch_size + 1} committed.")
    time.sleep(delay_seconds)  # Delay to avoid Firestore write limits

print("Update completed.")