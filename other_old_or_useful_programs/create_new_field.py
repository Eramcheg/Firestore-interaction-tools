import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase admin SDK with your credentials
source_cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
source_app = firebase_admin.initialize_app(source_cred, name='source_app')

db = firestore.client(app=source_app)

def get_new_user_id():
    @firestore.transactional
    def increment_user_id(transaction, user_counter_ref):
        snapshot = user_counter_ref.get(transaction=transaction)
        last_user_id = snapshot.get('lastUserId') if snapshot.exists else 3000
        new_user_id = last_user_id + 1
        transaction.update(user_counter_ref, {'lastUserId': new_user_id})
        return new_user_id

    metadata_collection = db.collection('metadata')
    user_counter_ref = metadata_collection.document('userCounter')
    transaction = db.transaction()
    new_user_id = increment_user_id(transaction, user_counter_ref)
    return new_user_id

# Iterate over each document in 'users' collection to assign userIds
users_collection = db.collection('users')
users_documents = users_collection.stream()

for doc in users_documents:
    # new_user_id = get_new_user_id()  # Get a unique userId for each user
    doc.reference.update({'Enabled': True})

print("Updated all documents with the registrationDate.")
# Get a Firestore client
# source_db = firestore.client(app=source_app)
#
# # Reference to the 'Products' collection
# source_collection = source_db.collection('users')
#
# # Fetch all documents in the 'Products' collection
# docs = source_collection.stream()
#
# # Iterate over the documents
# for doc in docs:
#     # Get the document data
#     doc_data = doc.to_dict()


    # # Check if 'image-urls' field exists and 'image_urls' field does not exist
    # if 'order-id' in doc_data and 'image_url' not in doc_data:
    #     # Read the value of 'image-urls'
    #     image_urls_value = doc_data['image-url']
    #
    #     # Update the document with the new field 'image_urls'
    #     update_data = {
    #         'image_url': image_urls_value,  # This will update or create 'image_url'
    #     }
    #
    #     # Firestore allows non-alphanumeric characters in field names, like hyphens, so this should work
    #     # update_data['image-url'] = image_urls_value
    #
    #     # Update the document with the new fields
    #     source_collection.document(doc.id).update(update_data)
    #     print(f"Document {doc.id} updated.")
    # else:
    #     print(f"Document {doc.id} already has 'image_urls' field or lacks 'image-urls'.")
