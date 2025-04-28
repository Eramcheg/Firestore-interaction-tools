from firebase_admin import credentials, firestore, initialize_app
from openpyxl import Workbook

# Инициализируем Firebase Admin с указанными учетными данными
cred = credentials.Certificate("G:\\FIles\\firebase\\key2.json")
initialize_app(cred)

# Получаем клиент Firestore
db = firestore.client()

# Делаем запрос к базе данных для получения документов, где customer_type != "B2B"
docs = db.collection("webUsers").stream()

# Определяем порядок колонок, который необходим для записи в Excel
ordered_keys = [
    'email',
    'first_name',
    'last_name',
    'social_title',
    'userId',
    'customer_type',
    'birthday',
    'registrationDate',
    'price_category',
    'currency',
    'Enabled',
    'receive_offers',
    'receive_newsletter',
    'show_quantities',
]

# Маппинг для преобразования заголовков в "нормальный вид"
header_map = {
    'email': 'Email',
    'special_customer': 'Special Customer',
    'userId': 'User ID',
    'agent_number': 'Agent Number',
    'b2b_can_pay': 'B2B Can Pay',
    'last_name': 'Last Name',
    'role': 'Role',
    'Enabled': 'Enabled',
    'receive_offers': 'Receive Offers',
    'birthday': 'Birthday',
    'social_title': 'Social Title',
    'registrationDate': 'Registration Date',
    'customer_type': 'Customer Type',
    'price_category': 'Price Category',
    'country': 'Country',
    'display_name': 'Display Name',
    'receive_newsletter': 'Receive Newsletter',
    'show_quantities': 'Show Quantities',
    'first_name': 'First Name',
    'sale': 'Sale',
    'currency': 'Currency'
}

# Создаем новый Excel файл и задаем активный лист
file_path = '../../../static_files/ow_export_data_folder/full_all_users16042025.xlsx'
workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Users"

# Записываем заголовки с преобразованием в читаемый вид
headers = [header_map.get(key, key) for key in ordered_keys]
worksheet.append(headers)

# Обрабатываем каждый документ и записываем данные по порядку колонок
for doc in docs:
    data = doc.to_dict()
    row = []
    for key in ordered_keys:
        val = data.get(key, "")
        # Если значение – булево, преобразуем его в "Yes" или "No"
        if isinstance(val, bool):
            val = "Yes" if val else "No"
        row.append(val)
    worksheet.append(row)

# Сохраняем файл
workbook.save(file_path)
print(f"Данные успешно записаны в {file_path}")
