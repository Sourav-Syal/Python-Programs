import csv

with open("olympics.csv", "r") as file_ref:
    reader = csv.DictReader(file_ref)
    print("LIST OF SPORTSPERSON WHO HAVE WON MEDALS")
    print("============================================")

    for row in reader:
        if row['Medal'] != 'NA':
            print(f"NAME: {row['Name']} \nEVENT: {row['Event']} \nMEDAL: {row['Medal']}")
            print("================")
