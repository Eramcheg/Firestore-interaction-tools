import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
collection_ref = firestore.client().collection("item")

docs = collection_ref.stream()

# Prepare data for backup
data_for_backup = [doc.to_dict() for doc in docs]

# Generate filename with today's date
today_date = datetime.now().strftime("%d.%m.%Y")
filename = f"item_backup_{today_date}.json"

# Write data to JSON file
with open(filename, "w", encoding="utf-8") as file:
    json.dump(data_for_backup, file, ensure_ascii=False, indent=4)

print(f"Backup created successfully: {filename}")