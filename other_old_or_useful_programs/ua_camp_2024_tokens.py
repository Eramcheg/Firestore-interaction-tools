from datetime import timedelta

import firebase_admin
from firebase_admin import credentials, firestore
import random
import string

# Initialize Firebase Admin using your specified credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\ukcamp2024.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

collection_ref = db.collection("actions")

collection_ref_users = db.collection("users")

def check_and_delete_duplicates():
    # Get all documents from the actions collection
    actions = collection_ref.get()

    # Dictionary to store actions by receiver
    actions_dict = {}

    # Populate the dictionary with actions
    for action in actions:
        action_data = action.to_dict()
        receiver = action_data['receiver']
        added_time = action_data['added_time']

        if receiver == " ":
            continue
        if action_data['group'] != "Код":
            continue
        if receiver not in actions_dict:
            actions_dict[receiver] = []

        actions_dict[receiver].append((action.id, added_time))

    # Iterate through the dictionary and check for duplicates
    for receiver, actions_list in actions_dict.items():
        actions_list.sort(key=lambda x: x[1])  # Sort by added_time

        for i in range(1, len(actions_list)):
            current_action_id, current_time = actions_list[i]
            previous_action_id, previous_time = actions_list[i - 1]

            # Check if the time difference is less than 20 minutes
            if current_time - previous_time < timedelta(minutes=2):
                # Delete the current action as it is a duplicate
                collection_ref.document(current_action_id).delete()
                print(f"Deleted duplicate action: {current_action_id} for receiver: {receiver}")
                last_space_index = receiver.rfind(' ')
                if last_space_index != -1:
                    name = receiver[:last_space_index]
                    surname = receiver[last_space_index+1:]
                    # Find the corresponding user document
                    user_query = collection_ref_users.where('name', '==', name).where('surname', '==', surname).limit(1)
                    user_docs = user_query.get()
                    if not user_docs:
                        user_query = collection_ref_users.where('name', '==', name).where('surname', '==',
                                                                                          surname+" ").limit(1)
                        user_docs = user_query.get()
                    if user_docs:
                        user_doc = user_docs[0]
                        user_data = user_doc.to_dict()
                        new_quantity = user_data['tokens'] - 1
                        collection_ref_users.document(user_doc.id).update({'tokens': new_quantity})
                        print(f"Decremented quantity for user: {name} {surname} to {new_quantity}")
                    else:
                        print(f"User {name} {surname} not found.")
                else:
                    print(f"Invalid receiver format: {receiver}")


# Run the function
check_and_delete_duplicates()

print("All documents have been updated with a unique random 5-digit string.")
