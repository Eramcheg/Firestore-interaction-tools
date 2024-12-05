from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image

# Создание документа
doc = SimpleDocTemplate("order_summary.pdf", pagesize=A4)
elements = []


# Логотип
logo_path = "../static_files/74.jpg"
elements.append(Image(logo_path, width=180, height=60))
elements.append(Spacer(1, 20))

# Заголовок
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1
elements.append(Paragraph("Thank you for shopping with Oliver Weber Shop.", title_style))
subtitle = "You'll find your Order Summary below. If you have any questions regarding your order, please contact us at 647.649.3912 ext. 5"
elements.append(Paragraph(subtitle, styles["Normal"]))
elements.append(Spacer(1, 20))
bold_style = styles["Normal"]
white_style = styles["Normal"]
white_style.fontColor = colors.white
bold_style.fontName = "Helvetica-Bold"
# Таблицы

order_data = [
    [Paragraph("<b>Order Status</b>", bold_style), "PROCESSING"],
    [Paragraph("<b>Order No</b>", bold_style), "1234234234"],
    [Paragraph("<b>Shipping Date</b>", bold_style), "12-10-2021"],
    [Paragraph("<b>Receipt </b>", bold_style), "10412"],
    ["", ""],
    [Paragraph("<b>Customer Code</b>", bold_style), "Stripe"],
    [Paragraph("<b>Date</b>", bold_style), "12-09-2021"]
]

# Данные для второй таблицы
contact_data = [
    [Paragraph("<b>Oliver Weber Collection</b>", bold_style), ""],
    ["", ""],
    ["Phone:", "+43 5223 41 881"],
    ["Email:", "office@oliverweber.at"]
]

# Создание таблиц
order_table = Table(order_data, colWidths=[120, 180])  # Ширина столбцов
contact_table = Table(contact_data, colWidths=[80, 220])

# Стили таблиц
order_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))

contact_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('SPAN', (0, 0), (1, 0)),  # Объединение ячейки для заголовка
]))

# Компоновка таблиц на одной строке
composite_table_data = [[order_table, contact_table]]

composite_table = Table(composite_table_data, colWidths=[250, 250])  # Общая ширина

# Установка общего стиля для компоновки
composite_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
elements.append(composite_table)
elements.append(Spacer(1, 20))

# Адреса
address_data = [
    ["Customer Billing Details", "Delivery Details"],
    ["Contact Phone:", "Ship-To Code: SHIP5"],
    ["Billing Address:", "Ship-To Name: David Owen"],
    ["1543 Bayview Ave", "Shipping Address: 40 Donegall Dr"],
    ["Toronto", "Toronto"],
    ["M4G 3B5", "M4G 3G5"],
    ["Ontario", "ON"],
    ["Canada", "CANADA"],
]

address_table = Table(address_data, colWidths=[250, 250])
address_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#003765")),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                                    ]))

elements.append(address_table)
elements.append(Spacer(1, 20))

# Примечания
comments = "Comments:<br/>Test order by commercebuild - Do not process!<br/>Shipping Via: 10PKUP - Store Pickup - Bayview - Orders placed before 3pm can be picked up same day"
elements.append(Paragraph(comments, styles["Normal"]))
elements.append(Spacer(1, 20))

# Таблица товаров
product_data = [
    ["Product", "Photo", "Item Details", "Quantity", "Unit Price", "Total"],
    ["12345G", "", "DE LA MER CARMELIZED ONION COD CAKES (5OZ)", "1", "CA$5.99", "CA$5.99"],
]

product_table = Table(product_data)
product_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#003765")),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                                   ]))

elements.append(product_table)
elements.append(Spacer(1, 20))

# Итоговая сумма
# Итоговая сумма
summary_data = [
    [Paragraph("<b>Subtotal</b>", bold_style), "CA$5.99"],
    [Paragraph("<b>VAT</b>", bold_style), "CA$0.00"],
    [Paragraph("<b>TOTAL</b>", bold_style), "CA$5.99"],
]

# Создание таблицы
summary_table = Table(summary_data, colWidths=[100, 100])  # Ширина столбцов

# Стилизация таблицы
summary_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),               # Выравнивание текста в ячейках
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),        # Шрифт текста
    ('FONTSIZE', (0, 0), (-1, -1), 10),                # Размер шрифта
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),            # Нижний отступ
    ('LINEBELOW', (0, 1), (-1, 1), 1, colors.black),   # Линия под строкой VAT
    ('LINEBELOW', (0, 2), (-1, 2), 1.5, colors.black), # Линия под строкой TOTAL
]))

# Добавление таблицы с отступом вправо
table_wrapper = Table([[summary_table]], colWidths=[doc.width])  # Внешняя таблица для отступа
table_wrapper.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),  # Выравнивание всей таблицы по правому краю
]))

# Добавление таблицы в элементы
elements.append(table_wrapper)

# Генерация PDF
doc.build(elements)
