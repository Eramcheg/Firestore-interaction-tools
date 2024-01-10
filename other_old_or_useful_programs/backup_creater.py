import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("G:\\FIles\\firebase\\key4_Terminal.json")
firebase_admin.initialize_app(cred)
collection_ref = firestore.client().collection("Product")

query = collection_ref.stream()

i = 0
for doc in query:
    i+=1
    if(i%10==0):
        print(i)
print("Finished with i = " + str(i))