import openpyxl
import csv
import io
import firebase_admin
from firebase_admin import credentials, firestore
import ftplib
import datetime


cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Reference the collection where you want to update the document
collection_ref = firestore.client().collection("Cart")

query = collection_ref.where("emailOwner", "==", "sur4i@abv.bg").stream()

for quer in query:
    print((quer.to_dict())['quantity'])

