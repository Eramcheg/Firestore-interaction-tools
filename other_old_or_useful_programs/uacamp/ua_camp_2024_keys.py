import firebase_admin
from firebase_admin import credentials, firestore
import random
import string

# Initialize Firebase Admin using your specified credentials
cred = credentials.Certificate("G:\\FIles\\firebase\\ukcamp2024.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

collection_ref_1 = db.collection("codes")
collection_ref = db.collection("admins")  # Specify your collection name
collection_ref_codes = db.collection("codes").document("array")

# Function to generate a random 5-digit string
def generate_random_string(length=5):
    return ''.join(random.choices(string.digits, k=length))

def get_constants():
    doc = collection_ref_1.get()
    if doc[0].exists:
        return doc[0].to_dict()
    else:
        return {"array_codes": [], "generation": 0}
# Get all documents in the collection

def update_constants(array_codes, generation):
    collection_ref_codes.update({
        "array_codes": array_codes,
        "generation": generation
    })
def update_admin_codes():
    constants = get_constants()
    array_codes = constants["array_codes"]
    generation = constants["generation"] + 1

    # Get all documents in the admin collection
    docs = collection_ref.stream()

    # Create a batch
    batch = db.batch()

    for doc in docs:
        # Generate a unique random 5-digit string
        while True:
            random_string = generate_random_string()
            if random_string not in array_codes:
                array_codes.append(random_string)
                break

        # Update the admin code in the batch
        doc_ref = collection_ref.document(doc.id)
        batch.update(doc_ref, {"admin_code": random_string})

    # Commit the batch
    batch.commit()

    # Check if generation should be reset
    if generation >= 20:
        array_codes = []
        generation = 0

    # Update the constants document
    update_constants(array_codes, generation)

# Example of running the update function
update_admin_codes()

print("All documents have been updated with a unique random 5-digit string.")
