import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db =firestore.client()
collection_ref = firestore.client().collection("item")
docs = collection_ref.stream()
batch = db.batch()
batch_counter = 0
# Iterate over each document
for doc in docs:
    doc_dict = doc.to_dict()  # Convert the document to a dictionary
    description = doc_dict.get("description", "").lower()  # Get the description field

    # Determine the plating based on the description
    if "ring" in description:
        stone = "White"
        if " m" in description:
            size = "M"
        elif " s" in description:
            size = "S"
        elif " xl" in description:
            size = "XL"
        elif " l" in description:
            size = "L"
        elif " xs" in description:
            size = "XS"
        else:
            size = "Without"
    # elif "rosegold" in description or "RG" in description:
    #     plating = "Rose Gold"
    # else:
    #     plating = "Without"

    # If a plating was determined, update the document

        batch.update(collection_ref.document(doc.id), {"size": size})
        batch_counter += 1
    if batch_counter >= 500:
        batch.commit()
        batch = db.batch()  # Start a new batch
        batch_counter = 0

if batch_counter > 0:
    batch.commit()
print("Update completed.")