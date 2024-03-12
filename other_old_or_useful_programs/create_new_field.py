import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase admin SDK with your credentials
source_cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
source_app = firebase_admin.initialize_app(source_cred, name='source_app')

# Get a Firestore client
source_db = firestore.client(app=source_app)

# Reference to the 'Products' collection
source_collection = source_db.collection('item')

# Fetch all documents in the 'Products' collection
docs = source_collection.stream()

# Iterate over the documents
for doc in docs:
    # Get the document data
    doc_data = doc.to_dict()

    # Check if 'image-urls' field exists and 'image_urls' field does not exist
    if 'image_url1' in doc_data and 'image_url' not in doc_data:
        # Read the value of 'image-urls'
        image_urls_value = doc_data['image_url1']

        # Update the document with the new field 'image_urls'
        update_data = {
            'image-url': image_urls_value,  # This will update or create 'image_url'
        }

        # Firestore allows non-alphanumeric characters in field names, like hyphens, so this should work
        # update_data['image-url'] = image_urls_value

        # Update the document with the new fields
        source_collection.document(doc.id).update(update_data)
        print(f"Document {doc.id} updated.")
    else:
        print(f"Document {doc.id} already has 'image_urls' field or lacks 'image-urls'.")
