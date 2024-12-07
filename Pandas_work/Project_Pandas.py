import pandas as pd
import numpy as np

hotels = pd.read_csv("hotel_booking_data.csv")

# Table for counts for each day of the week that people arrived.

def convert(day,month,year):
    return f'{day}-{month}-{year}'

# hotels['date']  = np.vectorize(convert)(hotels['arrival_date_day_of_month'], hotels['arrival_date_month'],hotels['arrival_date_year'])
#pd.to_datetime(hotels['date']).dt.day_name().value_counts()

hotels['total_stays'] = hotels['stays_in_week_nights'] + hotels['stays_in_weekend_nights']

#average number of stays in hotel
print(np.round(a = (hotels['total_stays'].mean()),decimals = 2))

#average cost for stays (total stays)
print(np.round(a = ((hotels['total_stays'] * hotels['adr']).mean()), decimals = 2))

