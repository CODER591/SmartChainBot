#this file contain class RequestProc

# "objects of this class, is created by Request Composer"
# that exist for requesting CoinMarketCap resourse

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#should be as universal as possible
class RequestProc:
    session = Session()
  # parameters as very dynamic value should be in execRequest
    def __init__(self, headers,key):
       self.headers = headers;
       self.headers['X-CMC_PRO_API_KEY']=key;


#returns json
# We should handle 500x errors, and prevent in any case 400x
    def execRequest(self,parameters,url):
        self.session.headers.update(self.headers)
        try:
            response = self.session.get(url, params = parameters)
            data = json.loads(response.text);  #find difference btw this and below variant
            #data = response.json();
            print(data) # should be removedб now, just for controle
            return data;
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return "";
