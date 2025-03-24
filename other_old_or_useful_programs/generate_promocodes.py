import csv
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import random
import string
import uuid

# Инициализация Firebase с использованием файла ключа
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("Promocodes")


def generate_promo_code():
    # Генерация 8-символьного кода (заглавные буквы и цифры)
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=8))


# Список для хранения данных промокодов для записи в CSV
promo_codes_list = []

# Генерация 100 промокодов
for _ in range(100):
    code = generate_promo_code()
    new_id = str(uuid.uuid4())  # генерация уникального идентификатора
    creation_time = datetime.utcnow()
    promo_data = {
        "b2b_only": False,
        "code": code,
        "creation_date": creation_time,
        "discount": 20,
        "expiration_date": None,
        "id": new_id,
        "is_active": True,
        "single_use": True,
        "type": "Full",
        "used_count": 0
    }

    # Добавление документа в Firestore
    collection_ref.document(new_id).set(promo_data)

    # Подготовка данных для CSV (приводим дату к строке)
    promo_codes_list.append({
        "code": promo_data["code"],
    })

# Запись данных в CSV-файл
csv_file = "../static_files/promocodes.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=promo_codes_list[0].keys())
    writer.writeheader()
    writer.writerows(promo_codes_list)

print("Успешно сгенерированы и записаны 100 промокодов в Firestore и CSV-файл:", csv_file)
