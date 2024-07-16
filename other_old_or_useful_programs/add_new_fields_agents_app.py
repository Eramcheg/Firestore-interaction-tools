import csv

import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = firestore.client().collection("item")
docs = collection_ref.stream()
batch = db.batch()
batch_counter = 0

query = collection_ref.where("category", "==","Post Earrings").get()
names = []
for doc in query:
    if "size" in doc.to_dict():
        doc_ref = collection_ref.document(doc.id)
        print(doc.to_dict())
        doc_ref.update({
            "size": firestore.DELETE_FIELD
        })
        print(f"Deleted 'size' field from document {doc.id}")
# with open('unmodified_names.csv', newline='', encoding="utf-8") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         names.append(row[0])  # Assuming the name is in the first column

# Stream documents and update
# batch = db.batch()
# batch_counter = 0
# docs = collection_ref.stream()

# for doc in docs:
# print(len(docs))
#     doc_dict = doc.to_dict()
#     # Check if the document's name field matches any name in the CSV
#     visibility = not doc_dict.get("name") in names
#     # Update the document with the new Visibility field
#     batch.update(doc.reference, {'Visible': visibility})
#     batch_counter += 1
#
#     # Commit the batch every 500 updates to avoid exceeding batch size limits
#     if batch_counter >= 500:
#         batch.commit()
#         batch = db.batch()  # Start a new batch
#         batch_counter = 0
#
# # Commit any remaining updates in the batch
# if batch_counter > 0:
#     batch.commit()
# Iterate over each document
# for doc in docs:
#     doc_dict = doc.to_dict()  # Convert the document to a dictionary
#     batch.update(collection_ref.document(doc.id), {
#         'social_title': "",
#         'first_name': "",
#         'last_name': "",
#         'birthday': "",
#         'country': "undefined",
#         "agent_number": "undefined",
#         'price_category': 'Default',
#         'receive_offers': False,
#         'receive_newsletter': False,
#         'addresses': [],
#         'favourites': [],
#     })
#     batch_counter += 1
#     if batch_counter >= 500:
#         batch.commit()
#         batch = db.batch()  # Start a new batch
#         batch_counter = 0
#
# if batch_counter > 0:
#     batch.commit()
print("Update completed.")