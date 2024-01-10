import firebase_admin
from firebase_admin import credentials, firestore

source_cred = credentials.Certificate("key4_Terminal.json")
source_app = firebase_admin.initialize_app(source_cred,name='source_app')

# Initialize the destination app
destination_cred = credentials.Certificate('terminaltests_key.json')
destination_app = firebase_admin.initialize_app(destination_cred,name="destination_app")

source_db = firestore.client(app=source_app)
destination_db = firestore.client(app=destination_app)


source_collection = source_db.collection('Languages')
destination_collection = destination_db.collection('Languages')

# Start copying documents
docs = source_collection.stream()
for doc in docs:
    doc_dict = doc.to_dict()
    destination_collection.document(doc.id).set(doc_dict)