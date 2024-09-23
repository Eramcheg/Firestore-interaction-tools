from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore
import random
import string

# Initialize Firebase Admin using your specified credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\ukcamp2024.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

collection_ref = db.collection("users")  # Specify your collection name

docs = collection_ref.stream()

# Current time for setting the 'break_until' field
current_time = datetime.now()

for doc in docs:
    data = doc.to_dict()

    if 'last_token' in data and 'break_until' in data:
        print(f"Skipping document {doc.id} as it already has 'last_token' and 'break_until' fields.")
        continue

    # Update the document with 'last_token' and 'break_until' fields
    collection_ref.document(doc.id).update({
        'last_token': "",
        'break_until': current_time
    })
