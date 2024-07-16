import os
import firebase_admin
from firebase_admin import credentials, storage
import re

# Path to your key.json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'flutterapp-fd5c3.appspot.com'
})

# Dictionary to store the image urls
urls = []

# DON'T TOUCH IT!
# This function uses blob for generating public image urls
def upload_file(file_path, destination_path, name):
    bucket = storage.bucket()
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    blob.make_public()
    urls.append(blob.public_url)
    print(f"File uploaded to {blob.public_url}")

# Function to extract numbers and sort numerically
def numerical_sort(value):
    # Извлекаем числа из строки
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])  # преобразуем числа
    return parts

directory_path = "G:\\FIles\\OliverWeber\\furnitureCatalog"
files = os.listdir(directory_path)
files.sort(key=numerical_sort)  # Sorting files numerically based on their names

# Iterating through all the images in the sorted list
for index, filename in enumerate(files, start=1):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        file_path = os.path.join(directory_path, filename)
        upload_file(file_path, f"2024PagesSummer/{filename}", filename[:-4])
        print(f"Uploaded {filename} to Firebase Storage.")

# Saving data
with open('../static_files/summerImages.txt', 'w') as file:
    for idx, url in enumerate(urls, start=1):
        file.write(f"//{idx+171}\n\"{url}\",\n\n")