import csv
fruit_price = {}
with open("../InventorySorting/Fruit_Price.csv", "r") as file_ref:
    reader = csv.reader(file_ref)
    temp_lst = list(reader)
    for lst in temp_lst[1:]:
        fruit_price[lst[0]] = lst[1]

fruit_quantity = {}
with open("../InventorySorting/Fruit_Quantity.csv", "r") as file_obj:
    reader = csv.DictReader(file_obj)
    temp_lst1 = list(reader)
    for dictionary in temp_lst1:
        fruit_quantity[dictionary['Item']] = dictionary['Quantity']

lst = list(fruit_price.keys())
temp_dict = {}
for key in lst:
    if key in fruit_quantity:
        temp_dict[key] = int(fruit_price[key]) * int(fruit_quantity[key])

lst_fruit = list(temp_dict.keys())
max_val = lst_fruit[0]
min_val = lst_fruit[1]
for key1 in lst_fruit:
    if temp_dict[key1] > temp_dict[max_val]:
        max_val = key1

    elif temp_dict[key1] < temp_dict[min_val]:
        min_val = key1

print("TOTAL INVENTORY COST AS PER ITEM (QUANTITY x COST):")
total = 0
for fruit in temp_dict:
    total += temp_dict[fruit]
    print(f"Value of {fruit} is {temp_dict[fruit]}")
print(f"TOTAL INVENTORY COST = {total}")

print(f"The costliest inventory is for the fruit '{max_val}'")
print(f"The cheapest inventory is for the fruit '{min_val}'")
