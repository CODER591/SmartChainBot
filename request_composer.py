# Reqeust Composer class
# composing request dynamically
# and creating objets of RequestProc, class

#composing request from url, setting dynamic params, headers, etc ...

from request import *


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
#headers, is dynamic value as much as http request
headers = {
  'Accepts': 'application/json',
  'Accept-Encoding': 'deflate, gzip',
  'X-CMC_PRO_API_KEY': 'here is your api key ',
}

new_req=RequestProc(headers,parameters,"key");
new_req.execRequest(url);
