import requests,os
import time,redis,json
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        proxy=''

        geojson='https://datahub.io/core/geo-countries/r/countries.geojson'
        geojson=' https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'

        proxyDict = { 
                    "http"  : proxy, 
                    "https" : proxy,
                    
                    }
        queue = redis.StrictRedis(host='redis', port='6379',db=1)
        while(True):
            response=requests.get(geojson)#,proxies=proxyDict)
            text=response.text
            
            x=json.loads(text)
            
            self.jsonpub(queue,x)
            time.sleep(10*60*60)

        
    def jsonpub(self,queue,inpjson):
        
        print("Publishing to redis",flush=True)
        queue.publish('countries.update', json.dumps(inpjson))
