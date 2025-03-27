import firebase_admin
from firebase_admin import credentials, firestore
from openpyxl import Workbook

# Initialize Firebase Admin using your specified credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Query the Firestore database
collection_ref = db.collection("item")  # Specify your collection name
query = collection_ref.where("Visible", "==", True)

docs = query.stream()

# Create a new Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Visible Items"

# Initialize the header with 'name' as the first column
headers = ["name"]
unique_fields = set(headers)

# Collect all unique field names across documents
for doc in docs:
    data = doc.to_dict()
    fields = list(data.keys())
    for field in fields:
        if field not in unique_fields:
            unique_fields.add(field)

# Write the complete header to the Excel sheet
ws.append(list(unique_fields))

# Reset the stream to iterate over documents again
docs = query.stream()

# Populate rows with data, filling missing fields with ""
for doc in docs:
    data = doc.to_dict()
    row = [data.get(field, "") for field in unique_fields]  # Use "" if field is missing
    ws.append(row)

# Save the workbook to an Excel file
wb.save('../static_files/visible_items.xlsx')

print("Excel file created successfully.")
