import openpyxl
import csv
import re
xlsx_file_path = "storages/30.11.2023.xlsx"

workbook = openpyxl.load_workbook(xlsx_file_path)

sheet = workbook.active

csv_file_path = 'storages/storage.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')

    csv_writer.writerow(['name', 'quantity'])

    # Iterate through rows in the XLSX sheet and extract data
    for row in sheet.iter_rows(min_row=2, values_only=True):
        name = row[4]  # Assuming 'name' is the 4th column (0-based index)

        quantity = row[2]  # Assuming 'quantity' is the 2nd column (0-based index)

        if quantity == None:
            quantity = 0
            print('quantity = 0')
        quantity = int(round(quantity, 0))

        if quantity< 0:
            quantity = 0
            print('quantity < 0')
        csv_writer.writerow([name, quantity])

print(f'CSV file saved at: {csv_file_path}')
