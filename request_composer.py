# Request Composer class
# composing request dynamically
# and creating objets of class RequestProc

#composing request from url, setting dynamic params, headers, etc ...
#composing depending on received value

#parameters are very much dynamic value.
import os

from headers import *
from parameters import *
from request import *

KEY= os.environ['COINCAPKEY']

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
# Type: class
# Name: RequestComposer
#
# Arguments:
#
# Functional: 
#   approppriate headers and parameters setting, making request by using RequestProc class
#class RequestComposer:
#    def __init__(self):


# Plans
# 1) Request composer composing request. So make switch that would choose/compose url;
# 2) Few things would be hardcoded, but nevermind
# 3) There is question, how to choose what request we need to send, what parameters we need?

new_req = RequestProc(GetBasicHeaders(),KEY);
#new_req.execRequest(Crypto_Map('active',1,5000,'name',symbol='',aux='platform'),url);
#new_req.execRequest(Crypto_Info(id='',slug='bitcoin',symbol='BTC',aux='platform'),url);
#new_req.execRequest(Crypto_List_Latest(start='1',limit='5000',volume_24h_min='500',convert='USD',convert_id='1',sort='name',sort_dir='asc',cryptocurrency_type='all',aux='platform'),url);
#new_req.execRequest(Crypto_List_Historical(date='2019-12-31',start='1',limit='5000',convert='USD',convert_id='1',sort='name',sort_dir='asc',cryptocurrency_type='all',aux='platform'),url);
new_req.execRequest(Crypto_Quotes_Latest(id='1',slug='bitcoin',symbol='BTC',
                          convert='USD',convert_id='',aux='platform',
                          skip_invalid='true'),url)
#
