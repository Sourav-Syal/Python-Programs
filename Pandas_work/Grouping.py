import pandas as pd
import numpy as np

mpg = pd.read_csv("mpg.csv")
year_cyl = mpg.groupby(['model_year','cylinders']).sum()[['mpg','displacement','horsepower','acceleration']]

print(year_cyl.loc[(70,4)]) #Able to fetch only one row of 4 cylinder car (can't access inner level directly)
print(year_cyl.xs(key=4,level="cylinders")) #Can fetch all year values of 4 cylinder car (inner level cross section)