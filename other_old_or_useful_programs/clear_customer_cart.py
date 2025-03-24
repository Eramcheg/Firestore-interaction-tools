from firebase_admin import credentials, firestore, initialize_app

# Инициализация Firebase
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
initialize_app(cred)
db = firestore.client()

# Удаление всех записей в коллекции "Cart" с "emailOwner" == "outlet@gmail.com"
def clear_cart_for_email(email):
    cart_ref = db.collection("Cart")
    query = cart_ref.where("emailOwner", "==", email).stream()

    deleted_count = 0
    for doc in query:
        print(f"Удаление документа с ID: {doc.id}")
        doc.reference.delete()
        deleted_count += 1

    print(f"Удалено {deleted_count} записей из коллекции 'Cart' для emailOwner: {email}")

# Очистить записи для указанного email
clear_cart_for_email("Outlet@gumpold.com")
