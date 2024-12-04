import csv
with open("ReducedOlympics.txt", "w") as file_ref:
    with open("olympics.csv", "r") as obj:
        reader = csv.reader(obj)
        rows = list(reader)
        file_ref.write("LIST OF SPORTSPERSON WHO HAVE WON MEDALS")
        file_ref.write('\n' + "======================" + '\n')

        for line in rows[1:]:
            if line[5] != 'NA':
                file_ref.write(f"NAME: {line[0]} \nEVENT: {line[4]} \nMEDAL: {line[5]}")
                file_ref.write("\n" + "======================" + "\n")