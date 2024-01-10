import openpyxl
import csv
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("key4_Terminal.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Reference to the Product collection
collection_ref = db.collection("Product")

# Fetch all documents from the Product collection
products = collection_ref.stream()

# Iterate over the products
for product in products:
    # Accessing the document data
    product_data = product.to_dict()

    # Check if the price field exists and then decrease it by 30%
    if 'group' in product_data:
        if product_data['group'] in ["2","3","4","5","6","7","8"]:
            if 'price' in product_data :
                # print(product_data['number'])
                # if product_data['category']!='Orologio':
                    old_price = product_data['price']
                    new_price = old_price * 0.5  # decrease by 20%
                    new_price = round(new_price)  # round to the nearest integer

                    # Update the document with the new price
                    product.reference.update({'price': new_price})

print("Price update completed.")
