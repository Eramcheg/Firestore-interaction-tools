import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
collection_ref = firestore.client().collection("item")
description_groups = {}
docs = collection_ref.stream()
for doc in docs:
    doc_data = doc.to_dict()
    description = doc_data.get("description", "")
    if description in description_groups:
        description_groups[description].append(doc_data)
    else:
        description_groups[description] = [doc_data]

# Step 3 and 4: Identify and print duplicates
for description, documents in description_groups.items():
    if len(documents) > 1:  # More than one document with the same description
        print(f"Duplicate description found: {description}")
        for doc in documents:
            print(json.dumps(doc, indent=4))  # Printing the document dat