import os

import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
def main_function(certificate, folder, app_name):
    # Initialize the Firebase app with a unique name
    try:
        # Try to get the Firebase app with the given app name
        app = firebase_admin.get_app(app_name)
        print(f"App {app_name} already initialized")
    except ValueError:
        # If the app is not initialized, initialize it
        cred = credentials.Certificate(certificate)
        firebase_admin.initialize_app(cred, name=app_name)
        print(f"App {app_name} initialized successfully")

        # Now we can access Firestore through the specified app
    db = firestore.client(firebase_admin.get_app(app_name))

    def serialize_value(value):
        """Recursively serialize Firestore data types to JSON serializable objects."""
        if isinstance(value, datetime):
            return value.isoformat()
        elif isinstance(value, firestore.DocumentReference):
            return value.path
        elif isinstance(value, list):
            return [serialize_value(v) for v in value]
        elif isinstance(value, dict):
            return {k: serialize_value(v) for k, v in value.items()}
        else:
            return value

    def serialize_firestore_document(doc):
        """Convert a Firestore document to a dictionary, handling Firestore data types."""
        doc_dict = doc.to_dict()
        return {key: serialize_value(value) for key, value in doc_dict.items()}

    # Prepare data for backup
    collections = db.collections()

    # Generate filename with today's date
    today_date = datetime.now().strftime("%d.%m.%Y")
    backup_folder = f"../{folder}/{today_date}/"

    # Ensure the backup directory exists
    os.makedirs(backup_folder, exist_ok=True)

    for collection in collections:
        docs = collection.stream()
        data_for_backup = [serialize_firestore_document(doc) for doc in docs]
        filename = f"backup_{collection.id}_{today_date}.json"
        full_path = os.path.join(backup_folder, filename)  # Combine the folder path and filename

        # Write data to JSON file
        with open(full_path, "w", encoding="utf-8") as file:
            json.dump(data_for_backup, file, ensure_ascii=False, indent=4)

        print(f"Backup created successfully: {full_path}")

firebases=[
    "G:\\FIles\\firebase\\key2.json",
    "G:\\FIles\\firebase\\uainternetolimp-41dd1-firebase-adminsdk-i78pu-fd374d92bc.json"
]
folders = ['firebase_backups_oliverweber', 'firebase_backups_uainternetolimp']

for idx, fireb in enumerate(firebases):
    app_name = f"app_{idx}"  # Generate a unique app name
    main_function(fireb, folders[idx], app_name)