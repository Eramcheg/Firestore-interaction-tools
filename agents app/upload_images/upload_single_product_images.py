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
dictionary = {}

def upload_file(file_path, destination_path, name):
    bucket = storage.bucket("flutterapp-fd5c3.appspot.com")
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    blob.make_public()
    dictionary[name] = blob.public_url
    print(f"File uploaded to {blob.public_url}")


# Путь к папке с изображениями
directory_path = r"C:\Users\eramc\Downloads\Image2504"
for filename in os.listdir(directory_path):
    if filename.endswith(".jpg") or filename.endswith(".png") :
        file_path = os.path.join(directory_path, filename) #NewImages/ было, нужно вставить это если использовать новые фотографии не для каталога
        upload_file(file_path, "NewImages/" + filename, filename[:-4])
        print(f"Uploaded {filename} to Firebase Storage.")
    elif filename.endswith(".jpeg"):
        file_path = os.path.join(directory_path, filename)
        upload_file(file_path, "NewImages/" + filename, filename[:-4])
        print(f"Uploaded {filename} to Firebase Storage.")


# Saving data
with open('../../static_files/image2504.txt', 'w') as file:
    file.write(str(dictionary))
