import openpyxl
from openpyxl import Workbook
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("G:\\FIles\\firebase\\uainternetolimp-41dd1-firebase-adminsdk-i78pu-fd374d92bc.json")
firebase_admin.initialize_app(cred)

# Reference the Firestore collection
db = firestore.client()
collection_ref = db.collection("users")

# Query to get documents where 'paralel' == '9'
query = collection_ref.where('paralel', '==', '10').where('role', '==', 'Student').stream()

# Create a new Excel workbook and add a sheet
wb = Workbook()
ws = wb.active
ws.title = "Обидва Тури 10 Клас Результати"

# Write the header
ws.append(["Ім'я", "Шифр", "Школа", "Електронна адреса", "Телефон", "Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5", "Сума 1 тур", "Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5", "Сума 2 тур", "Загальна сума"])

# Process each document in the query and write to the sheet
for doc in query:
    data = doc.to_dict()

    # Create Name column by combining first_name and last_name
    name = f"{data.get('first_name', '')} {data.get('last_name', '')} {data.get('third_name', '')}"
    id = data.get('userId', '')
    # Extract School
    school = data.get('school', '')
    email = data.get('email', '')
    phone = data.get('phone', '')

    # Calculate sum of grading arrays, default to 0 if field is missing
    task_1_sum = sum(data.get('task_1_grading', []))
    task_2_sum = sum(data.get('task_2_grading', []))
    task_3_sum = sum(data.get('task_3_grading', []))
    task_4_sum = sum(data.get('task_4_grading', []))
    task_5_sum = sum(data.get('task_5_grading', []))
    all_sum = task_1_sum + task_2_sum + task_3_sum + task_4_sum + task_5_sum

    task_1_sum_2 = sum(data.get('task_1_2_tour_grading', []))
    task_2_sum_2 = sum(data.get('task_2_2_tour_grading', []))
    task_3_sum_2 = sum(data.get('task_3_2_tour_grading', []))
    task_4_sum_2 = sum(data.get('task_4_2_tour_grading', []))
    task_5_sum_2 = sum(data.get('task_5_2_tour_grading', []))
    all_sum_2 = task_1_sum_2 + task_2_sum_2 + task_3_sum_2 + task_4_sum_2 + task_5_sum_2

    all_sum_all = all_sum + all_sum_2

    # Append the row to the sheet
    ws.append([name, id, school, email, phone, task_1_sum, task_2_sum, task_3_sum, task_4_sum, task_5_sum, all_sum, task_1_sum_2, task_2_sum_2, task_3_sum_2, task_4_sum_2, task_5_sum_2, all_sum_2, all_sum_all])

# Save the workbook
excel_file_path = "Обидва Тури 10 Клас Результати.xlsx"
wb.save(excel_file_path)

print("Excel file created successfully:", excel_file_path)
