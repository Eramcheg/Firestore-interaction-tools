import os
import firebase_admin
from firebase_admin import credentials, storage, firestore

# Path to your key2.json
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'flutterapp-fd5c3.appspot.com'
})

# Dictionary to store the image urls
dictionary = {}

# DON'T TOUCH IT!
# This function uses blob for generating public image urls
def upload_file(file_path, destination_path, name):
    bucket = storage.bucket("flutterapp-fd5c3.appspot.com")
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    blob.make_public()
    dictionary[name] = blob.public_url
    print(f"File uploaded to {blob.public_url}")


# Path to your folder with images
directory_path = "G:\\FIles\\newPhotosWInter24"

# Iterating through all the images in the folder
# Adding their public urls to dictionary
for filename in os.listdir(directory_path):
    if filename.endswith(".jpg"):
        file_path = os.path.join(directory_path, filename)
        upload_file(file_path, "NewImages/" + filename, filename[:-4])
        print(f"Uploaded {filename} to Firebase Storage.")

# Saving data
with open('../../static_files/new_image_urls.txt', 'w') as file:
    file.write(str(dictionary))
