import firebase_admin
from firebase_admin import credentials, firestore

# Инициализация Firebase Admin SDK
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Ссылка на коллекцию
collection_ref = firestore.client().collection("item")

# Запрос всех документов, где pre_order == true
query = collection_ref.where("pre_order", "==", True).stream()

# Обновление каждого документа
for doc in query:
    doc_id = doc.id
    print(doc.to_dict())# Получение ID документа
    print(f"Updating document ID: {doc_id}")  # Логирование обновления (по желанию)
    collection_ref.document(doc_id).update({"pre_order": False})

print("All documents with pre_order == true have been updated to pre_order == false.")
