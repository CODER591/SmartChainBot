#import json
#import requests

#global_url ='https://pro.coinmarketcap.com/migrate';

#request = requests.get(global_url);
#request = request.json();
#print(json.dumps(request,sort_keys=True,indent=4));

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
# so we sending http request to our  coincap api server
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '845c32ea-1b66-4337-9c1a-1ca477a40a4e',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #data = response.json();
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
