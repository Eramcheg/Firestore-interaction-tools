import json
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.transforms import ArrayUnion
# Инициализация Firebase
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Загружаем JSON со ссылками
with open('../../../static_files/images_for_products.json', 'r', encoding='utf-8') as f:
    images_dict = json.load(f)

for original_name, imgs in images_dict.items():
    # Сортируем записи по номеру картинки и берём только URL
    urls = [entry['url'] for entry in sorted(imgs, key=lambda x: x['img_num'])]

    # Обновляем массив additionalImages без дублирования
    query = db.collection('item').where("name", "==", original_name)
    docs = query.get()
    if not docs:
        print(f"⚠️ Документ с name='{original_name}' не найден.")
        continue

    for doc in docs:
        doc_ref = doc.reference
        # Вариант 1: использовать ArrayUnion
        doc_ref.update({
            'additionalImages': ArrayUnion(urls)
        })
        print(f"Updated '{original_name}' with {len(urls)} images.")