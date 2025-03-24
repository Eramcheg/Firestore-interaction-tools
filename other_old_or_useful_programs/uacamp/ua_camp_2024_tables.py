# import firebase_admin
# from firebase_admin import credentials, firestore
# import pandas as pd
# from collections import defaultdict
#
# # Initialize Firebase Admin using your specified credentials
# cred = credentials.Certificate("G:\\FIles\\firebase\\ukcamp2024.json")
# firebase_admin.initialize_app(cred)
#
# # Get a Firestore client
# db = firestore.client()
#
# collection_ref = db.collection("actions")
#
#
# def generate_excel_from_actions():
#     # Get all documents from the actions collection
#     actions = collection_ref.get()
#
#     # Dictionary to store the grouped data by receiver and group
#     grouped_data = defaultdict(lambda: defaultdict(int))
#
#     # Populate the dictionary with actions
#     for action in actions:
#         action_data = action.to_dict()
#         receiver = action_data.get('receiver', '')
#         group = action_data.get('group', '')
#         quantity = action_data.get('quantity', '')
#         operation = action_data.get('operation', '')
#         # Increment the count for the (receiver, group) pair
#         if receiver.strip() and group.strip():
#             if(operation=="відняла"):
#                 grouped_data[receiver][group] -= quantity
#             else:
#                 grouped_data[receiver][group] += quantity
#     # Create a list to hold the rows for the DataFrame
#     rows = []
#     last_receiver = None
#
#     for receiver, groups in grouped_data.items():
#         if last_receiver is not None and receiver != last_receiver:
#             rows.append({'receiver': '', 'group': '', 'quantity': ''})
#         for group, quantity in groups.items():
#             rows.append({
#                 'receiver': receiver,
#                 'group': group,
#                 'quantity': quantity
#             })
#         last_receiver = receiver
#
#     # Create a DataFrame
#     df = pd.DataFrame(rows, columns=['receiver', 'group', 'quantity'])
#
#     # Save the DataFrame to an Excel file
#     df.to_excel('actions_summary.xlsx', index=False)
#
#     print("Excel file 'actions_summary.xlsx' has been generated successfully.")
#
#
# # Run the function to generate the Excel file
# generate_excel_from_actions()

import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Initialize Firebase Admin using your specified credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\ukcamp2024.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Reference to the "users" collection
collection_ref = db.collection("users")

# Query all documents in the collection
docs = collection_ref.stream()

# Create a list of dictionaries to hold the data
data = []

for doc in docs:
    doc_dict = doc.to_dict()
    data.append({
        "name": doc_dict.get("name", ""),
        "surname": doc_dict.get("surname", ""),
        "email": doc_dict.get("email", ""),
        "tokens": doc_dict.get("tokens", 0)
    })

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by the 'tokens' column in descending order
df_sorted = df.sort_values(by="tokens", ascending=False)

# Save the DataFrame to an Excel file
file_path = "../uaolimp/Рейтинг.xlsx"
df_sorted.to_excel(file_path, index=False)

print(f"Excel file saved to: {file_path}")

