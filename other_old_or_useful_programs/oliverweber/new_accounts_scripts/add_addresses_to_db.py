import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

addrs_collection = db.collection('Addresses')

for i in range(1, 41):
    # Construct email
    email = f"customer{i}@oliverweber.at"

    # Construct address_id as counter + 1000000
    address_id = 1000000 + i

    # Data to be added to Firestore
    data = {
        'email': email,
        'address_id': address_id,
        'address_complement': "",
        'address_name': "Company",
        'city': 'Mils',
        'company': "Westa GmbH",
        'country': 'Austria',
        'first_name': "Oliver",
        'last_name': "Weber",
        'phone': '56556656',
        'postal_code': "6068",
        'real_address': "Gewerbepark Süd 24 "
    }

    # Add document to collection
    addrs_collection.add(data)

    print(f"Document created for {email} with address_id {address_id}")