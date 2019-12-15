# Request Composer class
# composing request dynamically
# and creating objets of class RequestProc

#composing request from url, setting dynamic params, headers, etc ...
#composing depending on received value

#parameters are very much dynamic value.
from parameters import *
from request import *
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
key = ''
'''parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}'''
headers = {
      'Accepts': 'application/json',
      'Accept-Encoding': 'deflate, gzip',
   }
# Type: class
# Name: RequestComposer
#
# Arguments:
#
# Functional: 
#   approppriate headers and parameters setting, making request by using RequestProc class
#class RequestComposer:
#    headers = {
#      'Accepts': 'application/json',
#      'Accept-Encoding': 'deflate, gzip',
#    }

#    def __init__(self):



#there is no need to add key in headers, it would be added in constructor


#move it to some command or wrapper, in any case remove this strings from this file
new_req=RequestProc(headers,key);
new_req.execRequest(Crypto_Map('active',1,5000,'name',symbol='',aux='platform'),url);
#new_req.execRequest(parameters,url);


# Request Compositor is a class that help us create as universal request
# as possible
# by seeting useful parameters and choose approppriate url
