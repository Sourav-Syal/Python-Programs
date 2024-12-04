import csv

price = open("Fruit_Price.csv", "r")
quantity = open("Fruit_Quantity.csv", "r")
final_result = open("Result_Set.csv", "w")

reader1 = csv.reader(price)
reader2 = csv.reader(quantity)

#Defining a function to write result set in a CSV file
def final(result_set):
    final_result.write('Item Name, Quantity, Price(per item), Total Amount')
    final_result.write('\n')
    tot = 0.0
    for row in result_set:
        tot = (int(row[2]) * float(row[1].replace("$","")))
        final_result.write(f"{row[0]}, {row[2]}, {row[1]}, {tot}")
        final_result.write('\n')

next(reader1)
next(reader2)

price_list = list(reader1)
quantity_list = list(reader2)

result_list = []

for ls in price_list:
    for line in quantity_list:
        if ls[0] == line[0]:
            result_list.append((ls[0], '$'+ls[1].strip(), line[1].strip()))

total_res = sorted(result_list, key = lambda t: int(t[2]) * float(t[1].replace("$","")))

#Calling the function based on sorted list created from the data of two different files
final(total_res)

#Closing file objects
price.close()
quantity.close()
final_result.close()