import csv

import firebase_admin
import openpyxl
from firebase_admin import credentials, firestore
from datetime import datetime
import json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Filepath to the Excel file
xlsx_file_path = "../../../agents app/storages/28.01.2025.xlsx"

# Load the Excel workbook
workbook = openpyxl.load_workbook(xlsx_file_path)
sheet = workbook.active

# Firestore collection reference
collection_ref = db.collection("item")

# Prepare to process Firestore batch updates
batch = db.batch()
batch_counter = 0
batch_size = 500  # Firestore limits the batch size

csv_file_path = "../../../static_files/updated_products.csv"
csv_columns = ['product_name', 'EAN']
def convert_to_float(value):
    if value is not None:
        # Replace commas with periods for decimal conversion
        try:
            return float(str(value).replace(',', '.'))
        except ValueError:
            return None
    return None
# Iterate through each row in the Excel file (skipping header row)
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row to the CSV file
    csv_writer.writerow(csv_columns)
    for row in sheet.iter_rows(min_row=2, values_only=True):  # start from second row
        product_name = row[4]  # E column
        product_width = convert_to_float(row[18])  # S column
        product_height = convert_to_float(row[19])  # T column
        chain_length = convert_to_float(row[21])  # V column
        ean_code = str(row[7])  # V column


        # Skip rows where product_name is None or empty
        if not product_name:
            continue

        try:
            # Query Firestore for documents where "name" equals the value from column E
            query = collection_ref.where("name", "==", product_name).get()

            for doc in query:
                doc_ref = collection_ref.document(doc.id)

                # Prepare the update data
                update_data = {}
                csv_row = [product_name]
                # Add product_width if it's not None or 0
                if ean_code is not None and ean_code != '':
                    update_data["ean_13"] = ean_code
                    csv_row.append(ean_code)
                else:
                    csv_row.append("")
                # Add product_width if it's not None or 0
                # if product_width is not None and product_width != 0 and product_width != '':
                #     update_data["product_width"] = float(product_width)
                #     csv_row.append(product_width)
                # else:
                #     csv_row.append("")
                #
                # # Add product_height if it's not None or 0
                # if product_height is not None and product_height != 0 and product_height != '':
                #     update_data["product_height"] = float(product_height)
                #     csv_row.append(product_height)
                # else:
                #     csv_row.append("")
                #
                # # Add chain_length if it's not None or 0
                # if chain_length is not None and chain_length != 0 and chain_length != '':
                #     update_data["chain_length"] = float(chain_length)
                #     csv_row.append(chain_length)
                # else:
                #     csv_row.append("")

                # Only perform the update if there's something to update
                if update_data:
                    batch.update(doc_ref, update_data)
                    batch_counter += 1

                    csv_writer.writerow(csv_row)

                # Commit the batch every 500 updates
                if batch_counter == batch_size:
                    batch.commit()
                    batch = db.batch()  # start a new batch
                    batch_counter = 0

        except Exception as e:
            print(f"Error processing product: {product_name} -> {e}")


# Commit any remaining updates in the batch
if batch_counter > 0:
    batch.commit()

print("Update completed!")