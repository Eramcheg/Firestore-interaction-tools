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
names2 = [
    "61322", "61324G", "62290", "62292G", "61320G", "61323G", "61321", "61321G", "61320", "62291G", "62289", "62289G",
    "12491G", "12493G", "12492G", "23214G", "23215G", "23216G", "12490G", "23213G", "41229S", "41229M","41229L", "41229XL", "41230S", "41230L", "41230M", "41230XL",
    "32432G", "12482G", "23205G", "32431", "23204", "12484", "23207", "23048", "12481",
    "12483G", "32433G", "23208G", "23206G", "12485G",
    "12489", "12488", "12487", "23212", "23211", "23210", "12486G", "12486", "23209G", "23209",
    "12157 L169I", "12157 L167I", "12157 L168I", "12157 L163I", "22916 L169I", "22916 L167I", "22916 L168I", "22916 L163I", "11522 971S", "11522 214", "22388 971S", "22388 214",
    "11523G 971S", "11523 1405", "11523 1201", "11523G 1002", "22389G 971S", "22389 1405", "22389 1201", "22389G 1002", "12052R 263", "12052R 238", "12052R 277", "22851R 263", "22851R 238", "22851R 277",
    "21009 L110D", "21009 1405", "21009 L134I", "21009 L107D", "21009 L169I", "21009 L142D", "21009 L167I", "21009 L163I", "21009 L168I", "21009 1201", "21009 L137I", "21009 L161I", "63322L BLU", "63322S BLU", "63322M BLU", "63322XL BLU"
]
# for name in names2:
query = collection_ref.where("pre_order", "==", True).get()

for doc in query:
    # if "size" in doc.to_dict():
    #     doc_ref = collection_ref.document(doc.id)
    #     print(doc.to_dict())
    #     doc_ref.update({
    #         "size": firestore.DELETE_FIELD
    #     })
    #     print(f"Deleted 'size' field from document {doc.id}")
    doc_ref = collection_ref.document(doc.id)
    dictionary = doc.to_dict()
    if dictionary.get('quantity', 0) > 0:
        print(f'{dictionary.get("name", "No name")} {dictionary.get("quantity", "NO QUANTITY")}')
        doc_ref.update({
            "pre_order": False
        })
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