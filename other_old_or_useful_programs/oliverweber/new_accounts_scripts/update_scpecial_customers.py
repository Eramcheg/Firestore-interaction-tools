import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# Loop through the specified range of emails
for i in range(1, 41):
    email = f'customer{i}@oliverweber.at'

    # Query to find the document with the specific email
    users_ref = db.collection('webUsers').where('special_customer', '==', True)
    docs = users_ref.stream()

    for doc in docs:
        # Update the document to add the 'special_customer' field
        doc.reference.update({'sale': 37.6})
        print(f"Updated user with email {email}.")