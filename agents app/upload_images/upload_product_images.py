import os
import json
import firebase_admin
from firebase_admin import credentials, storage

# Инициализация Firebase
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'flutterapp-fd5c3.appspot.com'
})

# Словарь: product_code → список URL’ов дополнительных картинок
images_dict = {}

def upload_file(file_path, destination_path):
    bucket = storage.bucket()
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    blob.make_public()
    return blob.public_url


# Путь к папке с изображениями
directory_path = r"C:\Users\eramc\Downloads\Image2504"

for filename in os.listdir(directory_path):
    name, ext = os.path.splitext(filename)
    if ext.lower() not in ('.jpg', '.jpeg', '.png'):
        continue

    parts = name.split('_')
    if len(parts) < 2:
        print(f"Пропускаем некорректное имя: {filename}")
        continue

    product_code = parts[0]
    img_num_part = parts[-1]
    # Всё между первым и последним — вариант (цвет, коллекция и т.п.)
    variant = "_".join(parts[1:-1]) if len(parts) > 2 else None

    try:
        img_num = int(img_num_part)
    except ValueError:
        print(f"Не распознан номер картинки в: {filename}")
        continue

    # Составляем оригинальное имя товара
    original_name = f"{product_code}{(' ' + variant) if variant else ''}"

    file_path = os.path.join(directory_path, filename)
    dest_path = f"NewImages/{product_code}/{filename}"
    url = upload_file(file_path, dest_path)
    print(f"Uploaded {filename} → {url}")

    entry = {'img_num': img_num, 'url': url}
    if variant:
        entry['variant'] = variant

    images_dict.setdefault(original_name, []).append(entry)

# Сохраняем результат в JSON, чтобы другой скрипт мог его загрузить
with open('images_for_products.json', 'w', encoding='utf-8') as f:
    json.dump(images_dict, f, ensure_ascii=False, indent=2)
print("Словарь URL’ов сохранён в images_for_products.json")
