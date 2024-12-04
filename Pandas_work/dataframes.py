import pandas as pd

#DataFrame using Dictionary
df = pd.DataFrame({'EmpID':[101,102,103,104,105,106],
                'EmpName':['Alex','Stuart','Anderson','Colt','Brew','Brown'],
                    'JobTitle':['Jr Engineer','Jr Engineer','HR','Sr Engineer','Sr Engineer','IT'],
                        'Salary':[45000,48000,32000,72000,75000,30000]})

#df.iloc[:5]

#Series from DataFrame using CSV File
age_df = pd.read_csv("../Files&Dictionaries/olympics.csv", usecols = ["Name","Age"], index_col = "Age")
age_series = age_df.squeeze("columns").copy()

#print(age_series.sort_index().head())

employees_series = pd.read_csv("../Files&Dictionaries/organizations-100.csv",
                               usecols = ["Number of employees"]).squeeze("columns")
#print(employees_series.describe())

org_df = pd.read_csv("../Files&Dictionaries/olympics.csv")

print(org_df.sort_values(by = ["Event","Name"], ascending = [False, True]))







