import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase admin SDK with your credentials
source_cred = credentials.Certificate("terminaltests_key.json")
source_app = firebase_admin.initialize_app(source_cred, name='source_app')

# Get a Firestore client
source_db = firestore.client(app=source_app)

# Reference to the 'Products' collection
source_collection = source_db.collection('Product')

# Fetch all documents in the 'Products' collection
docs = source_collection.stream()

# Iterate over the documents
for doc in docs:
    # Get the document data
    doc_data = doc.to_dict()

    # Check if 'image-urls' field exists and 'image_urls' field does not exist
    if 'image_urls' in doc_data and 'image-urls' not in doc_data:
        # Read the value of 'image-urls'
        image_urls_value = doc_data['image_urls']

        # Update the document with the new field 'image_urls'
        source_collection.document(doc.id).update({
            'image-urls': image_urls_value
        })
        print(f"Document {doc.id} updated.")
    else:
        print(f"Document {doc.id} already has 'image_urls' field or lacks 'image-urls'.")
