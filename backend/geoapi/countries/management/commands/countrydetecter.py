import redis,json,ast
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from countries.models import Country
class Command(BaseCommand):
    def handle(self, *args, **options):

        r = redis.StrictRedis(host='redis', port=6379, db=1)
        p = r.pubsub()
        p.psubscribe('countries.*')
        for message in p.listen():
            
            try:
                d=json.loads(message['data'])
                
                if d.get("type")=='FeatureCollection':
                    
                    geoinfo=d
                    for feature in geoinfo['features']:
                        if(feature['type']=='Feature'):
                            geom = GEOSGeometry(str(feature['geometry']))
                            if geom.geom_type == 'Polygon':
                                feature['geometry']['type']= 'MultiPolygon'
                                feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]
                            country=Country.objects.update_or_create(
                                name=feature['properties']['name'],
                                scene=GEOSGeometry(GEOSGeometry(str(feature['geometry'])))
                            )
            except Exception as e:
                print(e)
