import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

dates = [
    datetime(2020, 1, 22),
    datetime(2020, 1, 23),
    datetime(2020, 3, 23),
    datetime(2020, 3, 25),
    datetime(2020, 3, 27),
    datetime(2020, 3, 28)
    
]

y = [  0,1,1, 1, 1, 1]
plt.plot_date(dates,y, linestyle = 'solid',color = 'c',linewidth = ' 4')
plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)

# data = pd.read_csv('data.csv')
# price_date = data['Date']
# price_close = data['Close']

plt.title('Covid-19 Spikes')
plt.xlabel('Dates')
plt.ylabel('Numbers')

plt.tight_layout()

plt.show()