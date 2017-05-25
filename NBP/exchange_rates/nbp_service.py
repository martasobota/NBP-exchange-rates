import requests
from datetime import date, timedelta
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

# for rate in last_week:
# 	print(requests.get('http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + rate + '/?format=json').json())

def get_data(code):
    today = date.today()
    last_week = ["{:%Y-%m-%d}".format(today - timedelta(days=days_delta)) for days_delta in range(8)]	

    url = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + last_week[-1] + '/' + last_week[0] + '/?format=json').json()
    return url

    print("Url here: ")
    print(url)
    print('Items:')
    print(url.items())
    print('Test')
    print(url['rates'][0]['effectiveDate'])
    print(url['rates'][1])
    print(url['rates'][2])
    print(url['rates'][3])
    print(url['rates'][4])

# get_data('usd')


# # # # # # # # # # # # # # # # # # # # # # # # 

def create_table():
	global url
	print(url)

create_table()

# import plotly.plotly as py
# import plotly.figure_factory as ff

# data_matrix = [['Country', 'Year', 'Population'],
#                ['United States', 2000, 282200000],
#                ['Canada', 2000, 27790000],
#                ['United States', 2005, 295500000],
#                ['Canada', 2005, 32310000],
#                ['United States', 2010, 309000000],
#                ['Canada', 2010, 34000000]]

# table = ff.create_table(data_matrix)
# py.iplot(table, filename='simple_table')

# # # # # # # # # # # # # # # # # # # # # # # # 

# import plotly.plotly as py
# import plotly.graph_objs as go

# import pandas as pd

# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

# data = [go.Scatter(
#           x=df.Date,
#           y=df['AAPL.Close'])]

# py.iplot(data)
