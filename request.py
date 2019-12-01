#this file contain class RequestProc

# "objects of this class, is created by Request Composer"
# that exist for requesting CoinMarketCap resourse

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class RequestProc:
    session = Session()

    def __init__(self, headers, parameters,key):
       self.headers = headers; #this dictionary should compose automaticly with key
       self.parameters = parameters;
       self.key = key;

#returns json
#should handle 500 and 400 errors, or ReqComposer should prevent 400x errors
    def execRequest(self,url):
        self.session.headers.update(self.headers)
        try:
            response = self.session.get(url, params = self.parameters)
            data = json.loads(response.text);  #find difference btw this and below variant
            #data = response.json();
            print(data) # should be removedб now, just for controle 
            return data;
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return "";
