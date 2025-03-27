import csv
import openpyxl
from firebase_admin import credentials, firestore, initialize_app
from datetime import datetime
import json

# Инициализация Firebase
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
initialize_app(cred)
db = firestore.client()

# Путь к xlsx-файлу
xlsx_file_path = "../../../static_files/LBI 19.11.xlsx"

# Загрузка Excel-файла
workbook = openpyxl.load_workbook(xlsx_file_path)
sheet = workbook.active

# Пройтись по строкам Excel-файла
order_items = []
sum_price = 0

for row in sheet.iter_rows(min_row=2, values_only=True):  # min_row=2, чтобы пропустить заголовок
    name = str(row[0])  # Первый столбец - имя
    quantity = int(row[1])  # Второй столбец - количество

    if not name or not quantity:
        print(f"Пропуск строки с неполными данными: {row}")
        continue

    # Найти объект в коллекции "item" по имени
    item_ref = db.collection("item").where("name", "==", name).get()

    if not item_ref:
        print(f"Предмет с именем '{name}' не найден в коллекции 'item'. Пропуск.")
        continue

    # Получить данные из найденного объекта
    item = item_ref[0].to_dict()  # Предполагается, что имя уникально

    description = item.get("description", "")
    image_url = item.get("image_url", "")

    price = float(row[2])
    # price = item.get("priceVK3", 0)

    sum_price += price * quantity

    # Создать новый документ в коллекции "Order"
    order_data = {
        'description': description,
        'emailOwner': "ckbrown1@live.com",
        'image_url': image_url,
        'image-url': image_url,
        'name': name,
        'order_id': 45517005,  # Здесь можно задать уникальный ID, если требуется
        'order-id': 45517005,  # Дублирующий ID, как указано в задании
        'price': price,
        'quantity': quantity,
    }

    order_ref = db.collection("Order").document()
    order_ref.set(order_data)
    print(f"Создан заказ для '{name}' с количеством {quantity}.")

    # Добавить документ в список для коллекции Orders
    order_items.append(order_ref.path)

# Создать документ в коллекции Orders
# orders_data = {
#     'Status': 'Awaiting',
#     'date': datetime.now(),  # Current date and time
#     'email': "ckbrown1@live.com",
#     'list': [ref.reference.path for ref in order_items],  # Используем пути документов
#     'order_id': 248174027,
#     'order-id': 248174027,
#     'billingAddressId': "85504825",
#     'shippingAddressId': "85504825",
#     'price': round(float(sum_price), 2),
#     'shippingPrice': 0,
#     'VAT': 0,
#     'receipt_id': 10212,#177,
#     'currency': "Euro",
#     'payment_type': "BANK TRANSFER",
# }

orders_ref = db.collection("Orders")
# orders_ref = db.collection("Orders").document()
# orders_ref.set(orders_data)

query = orders_ref.where("order_id", "==", 45517005).limit(1)  # Ограничиваем результат до 1 документа
docs = query.stream()
for doc in docs:
    doc_ref = orders_ref.document(doc.id)  # Получаем ссылку на документ
    doc_ref.update({"list": order_items})  # Обновляем поле "list"
    print(f"Документ {doc.id} обновлён")
    break  # Останавливаем после первого найденного

# Если ничего не найдено
else:
    print("Документ с указанным order_id не найден")


print("Скрипт выполнен.")
