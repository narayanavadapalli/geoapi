import requests,os
import time

proxy=os.getenv("http_proxy","")

geojson='https://datahub.io/core/geo-countries/r/countries.geojson'
geojson=' https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'

proxyDict = { 
              "http"  : proxy, 
              "https" : proxy,
              
            }
def HandleJson(inpjson):
    print(inpjson)
while(True):
    response=requests.get(geojson,proxies=proxyDict)

    HandleJson(response.json())
    time.sleep(60*60*10)