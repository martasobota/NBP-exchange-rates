def get_data(code):
    url = 'http://api.nbp.pl/api/exchangerates/tables/B/?format=json' 
    params = {'code': code}
    r = requests.get('http://api.nbp.pl/api/exchangerates/tables/B/?format=json', params=params)
    nbp = r.json()
    nbp_list = {'nbp':nbp['results']}
