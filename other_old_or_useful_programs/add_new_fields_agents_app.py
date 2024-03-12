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

    category = "Default"
    # Determine the plating based on the description
    if "necklace" in description:
        category = "Necklaces"
    if "ring" in description or "anello" in description:
        category = "Rings"
    if "earrings" in description or "orrechini" in description:
        category = "Earrings"
    if "bracelet" in description or "braccialetto" in description:
        category = "Bracelets"
    if "pen" in description :
        category = "Accessories"
    if "watch" in description or "orologio" in description:
        category = "Accessories"
    batch.update(collection_ref.document(doc.id), {"category": category})
    batch_counter += 1
    if batch_counter >= 500:
        batch.commit()
        batch = db.batch()  # Start a new batch
        batch_counter = 0

if batch_counter > 0:
    batch.commit()
print("Update completed.")