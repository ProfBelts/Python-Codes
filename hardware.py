import pandas as pd
import csv
import copy

# top 10 items with most quantity
# number of items per category


hardware = pd.read_csv('hardwareStore.csv', index_col = 0)

top_10_quantity = hardware.nlargest(10, 'QUANTITY')

number_of_items = hardware.groupby('PRODUCT_NAME')['QUANTITY'].sum().sort_values(ascending = False)

print(top_10_quantity[['PRODUCT_NAME', 'QUANTITY']])

# print(number_of_items)
# 
# print(hardware)






# myHardWare = {
#     "category_id": "",
#     "category_name": "",
#     "product_id": "",
#     "description": "",
#     "description_detail_1" :"",
#     "description_detail_2" :"",
#     "description_detail_3" :"",
#     "description_detail_4" :"",
#     "standard_cost": "",
#     "list_price": "",
#     "country_id": "",
#     "region_id": "",
#     "location_id": "",
#     "warehouse_id": "",
#     "quantity": "",
#     "warehouse_name" : "",
#     "address": "",
#     "postal_code" : "",
#     "city": "",
#     "state": "",
#     "country_name": ""

# }

# myHardware= {

# }

# with open('hardwareStore.csv') as csvFile:
#     csvReader = csv.reader(csvFile, delimiter = ',')

#     for row in list(csvReader)[:]:
#         currentHardware = copy.deepcopy(myHardware)
#         currentHardware["category_id"] = row[0]
#         currentHardware["category_name"] = row[1] 
#         print(currentHardware["category_name"])

# hardware = pd.read_csv('hardwareStore.csv', index_col = 0)



