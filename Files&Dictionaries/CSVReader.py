import csv

with open("reduced_organizations.txt", "w") as fileobj:
    writer = csv.writer(fileobj)
    with open("organizations-100.csv", "r") as fileref:
        reader = csv.reader(fileref)
        temp_lst = list(reader)
        header = temp_lst[0]
        writer.writerow([header[1], header[3], header[5]])
        fileobj.write("==================================" + "\n")

        for rows in temp_lst[1:]:
            if rows[3] == 'Pakistan':
                writer.writerow([rows[1], rows[3], rows[5]])