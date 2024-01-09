import os
import firebase_admin
from firebase_admin import credentials, storage, firestore
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'flutterapp-fd5c3.appspot.com'
})

dictionary = {"e2r3": "https://codegeex.cn"}

# bucket = storage.bucket()
# image_name = "62223.jpg"
# blob = bucket.blob(image_name)
# if blob.exists():
#     future_date = datetime.now() + timedelta(days=365)
#     image_url = blob.generate_signed_url(expiration=future_date,version='v4')
#     print("Image URL:", image_url)
# else:
#     print("Image not found.")
# db = firestore.client()

# bucket = storage.bucket()
# blob = bucket.blob('imagesFolder/62223.jpg')
# blob.upload_from_filename('G:\\FIles\\Bilder\\62223.jpg')
# blob.make_public()
#here I'd like to have url of file I uploaded
# print(blob.public_url)
#
# import pyrebase
#
# # import pycryptodome
def upload_file(file_path, destination_path, name):
    bucket = storage.bucket("flutterapp-fd5c3.appspot.com")
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    blob.make_public()
    dictionary[name] = blob.public_url
    print(f"File uploaded to {blob.public_url}")

directory_path = "G:\\FIles\\newPhotosWInter24"
# bucket = storage.bucket("flutterapp-fd5c3.appspot.com")
i = 0
for filename in os.listdir(directory_path):
    if filename.endswith(".jpg"):
        # i+=1
        # if(i==5):
        #             break
        # print(filename[19:-4])
        file_path = os.path.join(directory_path, filename)
        upload_file(file_path, "NewImages/"+filename, filename[:-4])
        print(f"Uploaded {filename} to Firebase Storage.")

with open('../static_files/all_image_urls.txt', 'w') as file:
    file.write(str(dictionary))
# # # def get_all_images():
# # #     bucket = storage.bucket("flutterapp-fd5c3.appspot.com")
# # #     blobs = bucket.list_blobs()
# # #
# # #     image_urls = []
# # #     for blob in blobs:
# # #         if blob.content_type.startswith('image/'):
# # #             image_urls.append(blob.public_url)
# # #
# # #     return image_urls
# # #
# # # # Example usage
# # # all_images = get_all_images()
# # # for image_url in all_images:
# # #     print(image_url)
# #
# # bucket = storage.bucket()



# #
# # # List all files in the root folder
# # blobs = bucket.list_blobs()
# #
# # # Iterate through the blobs and print their URLs
# # for blob in blobs:
# #     if blob.name.endswith('.jpg') or blob.name.endswith('.jpeg') or blob.name.endswith('.png'):
# #         url = blob.generate_signed_url(expiration=300)  # Generate a signed URL for each image
# #         print(url)
# # # bucket = storage.bucket()
# # #
# # # # Iterate over all blobs in the storage bucket
# # # blobs = bucket.list_blobs()
# # #
# # # # Filter only image files and get their URLs
# image_urls = [blob.generate_signed_url(expiration=300) for blob in blobs if blob.content_type.startswith('image/')]
# # # i = 0100
# # # # Print the image URLs
# # # for url in image_urls:
# # #     i+=1
# # #     print(url)
# # # print(i)
# # firebaseConfig = {
# #
# #   "apiKey": "AIzaSyAM0wDc_WO0wP3-_TPRPLENZDIHbezH7U4",
# #
# #   "authDomain": "flutterapp-fd5c3.firebaseapp.com",
# #
# #   "projectId": "flutterapp-fd5c3",
# #     "databaseURL": "https://flutterapp-fd5c3.firebaseapp.com",
# #   "storageBucket": "flutterapp-fd5c3.appspot.com",
# #   "serviceAccount": "G:\\FIles\\firebase\\key2.json"
# #
# # }
# #
# # firebase_storage = pyrebase.initialize_app(firebaseConfig)
# # storage = firebase_storage.storage()
# # auth = firebase_storage.auth()
# # email = "westadatabase@gmail.com"
# # password = "Westa1234#"
# # user = auth.sign_in_with_email_and_password(email, password)
# # url = storage.child("62223.jpg").get_url(user['idToken'])
# # print(url)
# # # i = 0
# # # # Iterate through the files in the directory
# # # for filename in os.listdir(directory_path):
# # #     if filename.endswith(".jpg"):
# # #         if(i == 5):
# # #             break
# # #         i+=1
# # #         file_path = os.path.join(directory_path, filename)
# # #         storage.child("images/" + filename).put(file_path)
# # #         print(f"Uploaded {filename} to Firebase Storage.")
# # #
# #
# # # db = firestore.client()
# # # item_ref = db.collection('item')
# # # docs = item_ref.get()
# # #
# # # # Update the "quantity" field for each document
# # # i = 0
# # # batched_writes = []
# # #
# # # # Update the "quantity" field for each document
# # # for doc in docs:
# # #     doc_ref = item_ref.document(doc.id)
# # #     batched_writes.append(doc_ref.update({"quantity": random.randint(0, 100)}))
# # #     print(i)
# # #     i+=1
# # #
# # # # Execute the batched writes
# # # for batch in range(0, len(batched_writes), 500):
# # #     db.run_batch(batched_writes[batch:batch+500])
# # #
# # # print("All updates completed successfully.")
# # #
# # # #
# # # # bucket = storage.bucket()
# # # # blobs = bucket.list_blobs()
# # # #
# # # # for blob in blobs:
# # # #     if blob.name.endswith(('.jpg', '.jpeg', '.png')):
# # # #         # Do something with the image blob
# # # #         print(f"Image: {blob.name}")