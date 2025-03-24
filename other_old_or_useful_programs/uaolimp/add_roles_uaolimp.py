import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
cred = credentials.Certificate("G:\\FIles\\firebase\\uainternetolimp-41dd1-firebase-adminsdk-i78pu-fd374d92bc.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = firestore.client().collection("messages")
docs = collection_ref.stream()

# Текущая дата
today = datetime.now().date()

# Проходим по всем документам и проверяем timestamp
for doc in docs:
    data = doc.to_dict()
    # Предположим, что поле timestamp - это объект даты/времени
    if 'timestamp' in data:
        doc_date = data['timestamp'].date()
        # Если дата документа не совпадает с сегодняшней
        if doc_date != today:
            # Удаляем документ
            doc.reference.delete()
            print(f"Document {doc.id} deleted.")