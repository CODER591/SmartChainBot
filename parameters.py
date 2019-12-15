#End Points

#Main URL: https://pro-api.coinmarketcap.com/v1/
# cryptocurrency
#               map
#               info
#               listings/latest
#               listings/historical
#               quotes/latest
#''' Other options is not supported because of my free Basic plan '''

#Cryptocurrency
#Url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/"
        #map
def Crypto_Map(listing_status,start,limit,sort,symbol,aux):
        parameters={};
        #parameters['listing_status']=listing_status; #not allowed??
        parameters['start']=start;
        parameters['limit']=limit;
        parameters['sort']=sort;
        #parameters['symbol']=symbol;  #not allowed ???
        parameters['aux']=aux;
        return parameters;
#info
def Crypto_Info(id,slug,symbol,aux):
        parameters={};
        parameters['id']=id;
        parameters['slug']=slug;
        parameters['symbol']=symbol;
        parameters['aux']=aux;
        return parameters;
#listings/latest
def Crypto_List_Latest(start,limit,volume_24h_min,
                       convert,convert_id,sort,
                       sort_dir,cryptocurrency_type,aux):
        parameters={};
        parameters['start']=start;
        parameters['limit']=limit;
        parameters['volume_24h_min']=start;
        parameters['convert']=convert;
        parameters['convert_id']=convert_id;
        parameters['sort']=sort;
        parameters['sort_dir']=sort_dir;
        parameters['cryptocurrency_type']=cryptocurrency_type;
        parameters['aux']=aux;
        return parameters;
#listings/historical
def Crypto_List_Historical(date,start,limit,
                           convert,convert_id,sort,
                           sort_dir,cryptocurrency_type,aux):
        parameters={};
        parameters['date']=date;
        parameters['start']=start;
        parameters['limit']=limit;
        parameters['convert']=convert;
        parameters['convert_id']=convert_id;
        parameters['sort']=sort;
        parameters['sort_dir']=sort_dir;
        parameters['cryptocurrency_type']=cryptocurrency_type;
        parameters['aux']=aux;
        return parameters;
#quotes/latest
def Crypto_Qutotes_Latest(id,slug,symbol,
                          convert,convert_id,aux,
                          skip_invalid):
        parameters={};
        parameters['id']=id;
        parameters['slug']=slug;
        parameters['symbol']=symbol;
        parameters['convert']=convert;
        parameters['convert_id']=convert_id;
        parameters['aux']=aux;
        parameters['skip_invalid']=skip_invalid;
        return parameters;
