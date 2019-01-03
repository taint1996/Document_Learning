import pandas as pd
from datetime import date, datetime, timedelta
import moment

filename = '../test/twitter_tweets.csv'

df = pd.read_table(filename, skiprows=0, delimiter='\t', header=None, error_bad_lines=False)
d = df[1][1]
end_date = moment.date(d).subtract(days=1).add(hours=23, minutes=59, seconds=59)
start_date = moment.date(d).subtract(days=8).add(hours=23, minutes=59, seconds=59)

st_date = start_date.date
e_date = end_date.date

end = e_date.strftime("%Y-%m-%d %H:%M:%S")
start = st_date.strftime("%Y-%m-%d %H:%M:%S")

res = df[(df[1] >= start) & (df[1] <= end)]
