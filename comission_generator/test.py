product_info = {"Namee":"c"}

client_name = ""
if 'Name' in product_info.keys():
        client_name = product_info['Name']
else:
        client_name = "Cliente"
print(client_name)