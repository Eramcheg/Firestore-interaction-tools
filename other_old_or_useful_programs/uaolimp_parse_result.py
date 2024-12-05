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
query = collection_ref.where('paralel', '==', '11').where('role', '==', 'Student').stream()

# Create a new Excel workbook and add a sheet
wb = Workbook()
ws = wb.active
ws.title = "2 Тур 11 Клас"

# Write the header
ws.append(["Ім'я", "Школа", "Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5", "Всього"])

# Process each document in the query and write to the sheet
for doc in query:
    data = doc.to_dict()

    # Create Name column by combining first_name and last_name
    name = f"{data.get('first_name', '')} {data.get('last_name', '')}"

    # Extract School
    school = data.get('school', '')

    # Calculate sum of grading arrays, default to 0 if field is missing
    task_1_sum = sum(data.get('task_1_2_tour_grading', []))
    task_2_sum = sum(data.get('task_2_2_tour_grading', []))
    task_3_sum = sum(data.get('task_3_2_tour_grading', []))
    task_4_sum = sum(data.get('task_4_2_tour_grading', []))
    task_5_sum = sum(data.get('task_5_2_tour_grading', []))
    all_sum = task_1_sum + task_2_sum + task_3_sum + task_4_sum + task_5_sum

    # Append the row to the sheet
    ws.append([name, school, task_1_sum, task_2_sum, task_3_sum, task_4_sum, task_5_sum, all_sum])

# Save the workbook
excel_file_path = "2 Тур 11 Клас Результати.xlsx"
wb.save(excel_file_path)

print("Excel file created successfully:", excel_file_path)
