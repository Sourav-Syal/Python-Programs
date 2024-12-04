import pandas as pd

bigmac = pd.read_csv("bigmac.csv",
                     parse_dates = ["Date"], date_format = "%Y-%m-%d", index_col = ["Date", "Country"]).sort_index()

bigmac.loc[ ("2000-04-01","Argentina") : ("2000-04-01","Hungary") ]


