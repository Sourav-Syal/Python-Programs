import pandas as pd
tables = pd.read_html('https://en.wikipedia.org/wiki/World_population')
print(tables[5])

