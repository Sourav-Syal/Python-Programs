import pandas as pd
import numpy as np
tips = pd.read_csv("tips.csv")

def quality(total_bill,tip):
    if tip/total_bill > 0.25:
        return "Generous"
    else:
        return "Others"

#multiple column use with lambda function for apply method
tips['Quality'] = tips[['total_bill','tip']].apply(lambda df:quality(df['total_bill'],df['tip']), axis=1)

#using vectorize method to implement the same method
tips['Quality'] = np.vectorize(quality)(tips['total_bill'],tips['tip'])

