import csv
import copy


pattern = {
    "CATEGORY_ID": "",
    "CATEGORY_NAME": "",
    "PRODUCT_ID": "",
    "PRODUCT_NAME": 0,
    "QUANTITY": 0,
    "LIST_PRICE": 0,

}

items = []
category_sums = {}

with open('hardwareStore.csv') as file:
    reader = csv.reader(file, delimiter=',')

    for row in list(reader)[1:]:
        element = copy.deepcopy(pattern)
        element['CATEGORY_ID'] = row[0]
        element['CATEGORY_NAME'] = row[1]
        element['PRODUCT_ID'] = row[2]
        element['PRODUCT_NAME'] = row[3]
        element['QUANTITY'] = int(row[15])
        element['LIST_PRICE'] = row[10]
        items.append(element)

sorted_data = sorted(items, key=lambda x: x['QUANTITY'], reverse=True)

top_10_highest = sorted_data[:10]

for item in top_10_highest:
    print(f"Top 10 items with higer quantity: {item['PRODUCT_NAME']}")

for item in items:
    category = item['CATEGORY_NAME']
    quantity = item['QUANTITY']
    if category in category_sums:
        category_sums[category] += quantity
    else:
        category_sums[category] = quantity

for category, total_quantity in category_sums.items():
    print(f'Category {category}: Total Quantity = {total_quantity}')


# CATEGORY_ID
# CATEGORY_NAME
# PRODUCT_ID
# PRODUCT_NAME
# DESCRIPTION
# DESCRIPTION - Detail 1
# DESCRIPTION - Detail 2
# DESCRIPTION - Detail 3
# DESCRIPTION - Detail 4
# STANDARD_COST
# LIST_PRICE
# COUNTRY_ID
# REGION_ID
# LOCATION_ID
# WAREHOUSE_ID
# QUANTITY
# WAREHOUSE_NAME
# ADDRESS,POSTAL_CODE,CITY,STATE,COUNTRY_NAME
