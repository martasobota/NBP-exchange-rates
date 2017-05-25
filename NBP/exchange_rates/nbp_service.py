import requests
from datetime import date, timedelta
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

def get_7_working_days():
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
	return last_days

def get_data(code):	
	url = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + last_days[-1] + '/' + last_days[0] + '/?format=json').json()
	return url

def create_matrix(url):
	data = []
	for u in url['rates'][-7:]:
		data.append(u)
	ex_rates_matrix = [['Date', 'Rate'], ]
	for r in data:
		plus = []
		plus.append(r['effectiveDate'])
		plus.append(r['mid'])
		ex_rates_matrix.append(plus)

	rates_table = np.matrix(ex_rates_matrix)

	'''
	Prints table with exchange rates data usd/pln for last 7 working days
	'''
	print(rates_table)

	'''
	Creates chart with data from matrix
	'''
	table = ff.create_table(ex_rates_matrix)
	py.plot(table, filename='ex_rates_7days_usd_table')

last_7 = get_7_working_days()
get_data('usd', last_7)
rate_data = get_data('usd')
create_matrix(rate_data)
