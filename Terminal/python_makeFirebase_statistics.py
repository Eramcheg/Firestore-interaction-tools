import firebase_admin
from firebase_admin import credentials, firestore
import csv
cred = credentials.Certificate("G:\\FIles\\firebase\\key4_Terminal.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("Orders")
order_summary = {}

# Iterate over each document in the 'Orders' collection
for order_doc in collection_ref.stream():
    order_data = order_doc.to_dict()
    if order_data.get('Status') == 'Paid':
        # Iterate over the references in the 'list' field
        for order_ref in order_data.get('list', []):
            # Dereference the document
            order = order_ref.get().to_dict()

            # Extract 'number' and 'quantity'
            order_number = order.get('number')
            order_quantity = order.get('quantity', 0)
            order_sum = order.get('price', 0) * order_quantity

            # Add to the dictionary, summing the quantities for duplicate numbers
            if order_number in order_summary:
                order_summary[order_number][0] += order_quantity
                order_summary[order_number][1] += order_sum
            else:
                order_summary[order_number] = [order_quantity, order_sum]

# Print or process the order_summary dictionary
print(order_summary)
with open('../static_files/statistics11_03_2024.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['number', 'quantity', 'sum'])

    # Write the data
    for number, items in order_summary.items():
        writer.writerow([number, items[0], items[1]])

print("CSV file created successfully.")