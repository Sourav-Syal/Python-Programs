import csv
def read_func(read_obj):
    reader = csv.reader(read_obj)
    next(reader)
    return list(reader)

with open("../InventorySorting/Fruit_Quantity.csv", "r") as file_ref:
    item_list = read_func(file_ref)

    result_set = sorted((dict(filter(lambda t: t if int(t[1]) > 15 else "", item_list))),
                        key = lambda k: len(k))
    idx = 1
    for items in result_set:
        print(f"{idx}.{items}")
        idx += 1