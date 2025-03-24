import openpyxl
from openpyxl import Workbook
import firebase_admin
from firebase_admin import credentials, firestore, storage

# Initialize Firebase
cred = credentials.Certificate("G:\\FIles\\firebase\\uainternetolimp-41dd1-firebase-adminsdk-i78pu-fd374d92bc.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'uainternetolimp-41dd1.appspot.com'
})

local_file_path = "C:\\Users\\eramc\\Downloads\\Telegram Desktop\\task5.pdf"  # замените на путь к вашему файлу
blob_name = "users_files/student21_8a22@lpml.com.ua_Task_2_5.pdf_2_tour_123456"  # путь и имя файла в хранилище


# Функция для загрузки файла в Firebase Storage и получения публичной ссылки
def upload_file_to_firebase(local_path, storage_path):
    # Получаем bucket из Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(storage_path)

    # Загружаем файл
    blob.upload_from_filename(local_path)

    # Делаем файл публичным
    blob.make_public()

    # Получаем публичный URL
    public_url = blob.public_url
    return public_url


# Загрузка файла и получение ссылки
public_link = upload_file_to_firebase(local_file_path, blob_name)
print(f"Публичная ссылка на файл: {public_link}")
