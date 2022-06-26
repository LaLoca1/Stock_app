import requests

headers = {
    'Content-Type' : 'application/json', 
    'Authorization' : 'Token fbf96e3fb34e834b8089d28da00b49258408baa6'
}

def get_meta_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
    response = requests.get(url, headers=headers) 
    return response.json() 

def get_price_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
    response = requests.get(url, headers=headers) 
    return response.json()[0]

