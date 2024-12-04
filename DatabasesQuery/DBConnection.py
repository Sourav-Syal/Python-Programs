import sqlite3

con = sqlite3.connect("SQLiteMagic.db")
cur = con.cursor()

cur.execute('''SELECT COUNT(country), country, MIN(test_score) FROM INTERNATIONAL_STUDENT_TEST_SCORES GROUP BY country HAVING COUNT(country) > 1''')
temp_lst = cur.fetchall()

sort_list = (sorted(temp_lst, key = lambda tuples: (tuples[0], tuples[2], tuples[1])))
print("HERE ARE LIST OF STUDENTS FROM COUNTRIES WHERE WE HAVE MORE THAN ONE STUDENT:")
for tp in sort_list:
    print(f"{tp[0]} students are from '{tp[1]}' with min individual test score {tp[2]}")

con.commit()


