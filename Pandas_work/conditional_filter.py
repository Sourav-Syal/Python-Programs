import pandas as pd

#reading a file for movie collection

office = pd.read_csv("the_office.csv", parse_dates = ["Airdate"])

#converting data types
office["Director"] = office["Director"].astype("category")
office["Writer"] = office["Writer"].astype("category")
office["Season"] = office["Season"].astype("category")
office["Episode"] = office["Episode"].astype("category")
office["Name"] = office["Name"].astype(str)

#creating conditions for filtering data in data frame
after_2004 = office["Airdate"] > "01/01/2008"
by_ken = office["Director"] == "Ken Kwapis"
view_8 = office["Viewership"] >= 8.0

result = office[after_2004 & by_ken | view_8]
#print(result[["Name", "Airdate"]].sort_values(by = "Airdate", ascending = False))

#Reading another file for april month weather

temp_april = pd.read_csv("Temperature.csv", parse_dates = ["Day"])
print(temp_april[temp_april["Day"].between("04/02/2022","04/03/2022")])




