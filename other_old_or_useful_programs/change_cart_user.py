import openpyxl
import csv
import io
import firebase_admin
from firebase_admin import credentials, firestore
import ftplib
import datetime
# Initialize Firebase Admin with your service account credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# Reference the collection where you want to update the document
collection_ref = firestore.client().collection("Orders")

orders = {}
query = collection_ref.where('order_id', '==', 40576720)

# Execute the query
docs = query.stream()

# Iterate through the query results and update each document
for doc in docs:
    # doc_id = doc.id
    # # Update the email field
    # collection_ref.document(doc_id).update({'emailOwner': 'aida.suljevic@nall.me'})
    orders=(doc.to_dict())

print(orders)
