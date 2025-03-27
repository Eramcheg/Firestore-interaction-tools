import openpyxl
import firebase_admin
from firebase_admin import credentials, firestore

# Инициализация Firebase Admin
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("item")

# Путь к Excel‑файлу
xlsx_file_path = "../../../static_files/springproducts.xlsx"
workbook = openpyxl.load_workbook(xlsx_file_path)
sheet = workbook.active

# Первая строка – заголовки
headers = [cell.value for cell in sheet[1]]

# Обход строк (начиная со второй, где данные товаров)
for row in sheet.iter_rows(min_row=2, values_only=True):
    product_data = dict(zip(headers, row))

    # Преобразование столбцов с ценами к float
    price_columns = ["price", "priceGH", "priceUSD", "priceUSD_GH", "priceVK3", "priceVK4"]
    for col in price_columns:
        try:
            product_data[col] = float(product_data[col])
        except (TypeError, ValueError):
            product_data[col] = 0.0

    # Приведение quantity к целому числу
    try:
        product_data["quantity"] = int(product_data["quantity"])
    except (TypeError, ValueError):
        product_data["quantity"] = 0
    product_data["Visible"] = product_data["Visible"] == "True"
    # Приведение stone к строке
    if product_data.get("stone") is None:
        product_data["stone"] = ""
    else:
        product_data["stone"] = str(product_data["stone"])

    # Удаляем поля, если их значение пустое (None или пустая строка)
    product_data = {k: v for k, v in product_data.items() if v not in ("", None)}

    # Определяем идентификатор документа (например, по полю "name")
    doc_id = product_data.get("name")
    if doc_id:
        collection_ref.document(doc_id).set(product_data)
    else:
        collection_ref.add(product_data)

print("Товары успешно загружены в Firestore!")
