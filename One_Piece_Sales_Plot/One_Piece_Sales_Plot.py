import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter

year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
sales = [5956540, 14721241, 32343809, 37995373, 23464866, 18151599, 11884947, 14102521, 12314326, 
         11495532, 8113317, 10134232, 7709667, 7002583, 10364102]

def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fM' % (x * 1e-6)

formatter = FuncFormatter(millions)

plt.gca().yaxis.set_major_formatter(formatter)
plot = plt.plot(year, sales, color='#D32F2F', marker=".", linestyle='solid')
plt.title('One Piece Sales', fontsize=14, font="Product Sans")
plt.xlabel('Year', fontsize=10, font="Product Sans")
plt.ylabel('Sales (in millions)', fontsize=10, font="Product Sans")
plt.grid(True)
plt.show()