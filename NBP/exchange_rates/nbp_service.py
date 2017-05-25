import requests
from datetime import date, timedelta
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

def get_data(code):
	"""
	Creates table with dates in proper format (ISO 8601)
	Range = 15, to save dates with surplus, e.g. if you are checking exchange rates for last 7 days on Thursday, 
	you will need last 9 dates (there is weekend in between), but if you wanna check exchange rates on Monday 
	or Tuesday you will need dates for last 11 days, because there are two weekends in between.
	There are times during the year when there are also holidays, so range should be increased. 
	Value 15 is my prediction, if I would have more time I would try do it more accurate
	"""
	today = date.today()
	last_days = ["{:%Y-%m-%d}".format(today - timedelta(days=days_delta)) for days_delta in range(15)]	
	url = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + last_days[-1] + '/' + last_days[0] + '/?format=json').json()
	print(url)
	# return url

	data = []
	for u in url['rates'][-7:]:
		data.append(u)

	ex_rates_matrix = [['Date', 'Rate'], ]

	print('proper dates:')
	print(data)
	print(len(data))
	print(type(data))
	for p in data:
		plus = []
		plus.append(p['effectiveDate'])
		plus.append(p['mid'])
		ex_rates_matrix.append(plus)

	print(ex_rates_matrix)

	print("Matrix test:")
	print(np.matrix(ex_rates_matrix))

	# table = ff.create_table(ex_rates_matrix)
	# # py.iplot(table, filename='simple_table')
	# py.plot(table, filename='ex_rates_7days_table')

get_data('usd')



# # # # # # # # # # # # # # # # # # # # # # # # 

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
