import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Reference the collection where you want to update the document
db = firestore.client()

# Reference the collection
collection_ref = db.collection("item")

# Create a batch
batch = db.batch()
batch_count = 0
batch_limit = 500  # Maximum batch size

for doc in collection_ref.stream():
    doc_dict = doc.to_dict()
    if 'image-url' in doc_dict:
        # Add update operation to the batch
        batch.update(collection_ref.document(doc.id), {
            'image_url': doc_dict['image-url']
        })
        batch_count += 1

        # Commit the batch if limit reached and start a new batch
        if batch_count >= batch_limit:
            batch.commit()
            batch = db.batch()
            batch_count = 0

# Commit any remaining operations in the last batch
if batch_count > 0:
    batch.commit()