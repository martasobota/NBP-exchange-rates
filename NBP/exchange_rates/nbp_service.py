import requests
from datetime import date, timedelta

def get_data(code):
	last_week = []
	today = date.today()
	last_week.append("{:%Y/%m/%d}".format(today))

	day = today - timedelta(days=1)
	for d in range(7):
		last_week.append("{:%Y/%m/%d}".format(day))
		day -= timedelta(days=1)


	# return requests.get('http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + today + '/' + last_week[-1] + '/?format=json').json()
# for rate in last_week:
# 	print(requests.get('http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + rate + '/?format=json').json())

# return requests.get('http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + date.now -  + '/' + today + '/?format=json').json()
get_data('usd')