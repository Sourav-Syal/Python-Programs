import pandas as pd
tips = pd.read_csv("tips.csv")

#print(tips['total_bill'].apply(lambda num:num*2))

def quality(total_bill,tip):
    if tip/total_bill > 0.25:
        return "Generous"
    else:
        return "Others"

print(tips[['total_bill','tip']].apply
      (lambda df:quality(df['total_bill'],df['tip']), axis=1))