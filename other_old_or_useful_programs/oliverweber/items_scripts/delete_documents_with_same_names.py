import openpyxl
import csv
import io
import firebase_admin
from firebase_admin import credentials, firestore
import ftplib
import datetime

cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# List of duplicate names
duplicate_names = ['S24011 262', '41065GS', '12375RG', '12375', '41191RGS', '63239RL', 'S24006 209', '63542RG PIN', 'S24014 769', '22628R', '63289L', '41191RGL', '41191RGM', 'S24015 769', '41065GM', '23100', '41065GXL', '22813R', '41065GL', '63289M', '22426G', '41191RGXL']

# Process each name in the duplicate names list
for name in duplicate_names:
    # Query documents by name where 'priceVK4' field does not exist
    query = db.collection('item').where('name', '==', name)
    docs = query.stream()

    # Delete documents
    for doc in docs:
        if ('priceVK4' in doc.to_dict()):
            pass
        else:
            print(f"Deleting document with ID: {doc.id} and name: {name}, {doc.to_dict()}")
            doc.reference.delete()

print("Deletion complete.")