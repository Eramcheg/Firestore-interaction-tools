import openpyxl
import csv
import io
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)

# Reference the collection where you want to update the document
collection_ref = firestore.client().collection("Addresses")

# Функция для обновления типа поля address_id
def update_address_id_to_string():
    # Получение всех документов из коллекции
    docs = collection_ref.stream()

    for doc in docs:
        data = doc.to_dict()

        # Проверяем, есть ли поле address_id и если оно числовое
        if 'address_id' in data and isinstance(data['address_id'], (int, float)):
            # Преобразуем значение address_id в строку
            new_address_id = str(data['address_id'])
            # Обновляем документ в Firestore
            collection_ref.document(doc.id).update({'address_id': new_address_id})
            print(f"Updated document {doc.id} with address_id: {new_address_id}")
        else:
            print(f"No change required for document {doc.id}")


# Выполнение функции
update_address_id_to_string()