import os

import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
# collection_ref = firestore.client().collection("item")
db = firestore.client()

def serialize_value(value):
    """Recursively serialize Firestore data types to JSON serializable objects."""
    if isinstance(value, datetime):
        return value.isoformat()
    elif isinstance(value, firestore.DocumentReference):
        return value.path
    elif isinstance(value, list):
        return [serialize_value(v) for v in value]
    elif isinstance(value, dict):
        return {k: serialize_value(v) for k, v in value.items()}
    else:
        return value

def serialize_firestore_document(doc):
    """Convert a Firestore document to a dictionary, handling Firestore data types."""
    doc_dict = doc.to_dict()
    return {key: serialize_value(value) for key, value in doc_dict.items()}

# Prepare data for backup
collections = db.collections()

# Generate filename with today's date
today_date = datetime.now().strftime("%d.%m.%Y")
backup_folder = f"../firebase_backups/{today_date}/"

# Ensure the backup directory exists
os.makedirs(backup_folder, exist_ok=True)

for collection in collections:
    docs = collection.stream()
    data_for_backup = [serialize_firestore_document(doc) for doc in docs]
    filename = f"backup_{collection.id}_{today_date}.json"
    full_path = os.path.join(backup_folder, filename)  # Combine the folder path and filename

    # Write data to JSON file
    with open(full_path, "w", encoding="utf-8") as file:
        json.dump(data_for_backup, file, ensure_ascii=False, indent=4)

    print(f"Backup created successfully: {full_path}")
