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

query = collection_ref.where("name", ">","KS").get()
names = []
for doc in query:
    if doc.to_dict().get("name")[0] == "K":
        names.append(doc.to_dict().get("name")  )
print(names)