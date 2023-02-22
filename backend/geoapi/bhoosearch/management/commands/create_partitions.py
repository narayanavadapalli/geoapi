from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import psycopg2,calendar
from datetime import datetime,timedelta

class Command(BaseCommand):
    help = 'Creates the partitions for metnioned'

    def add_arguments(self, parser):
        parser.add_argument('start_date',  type=str,help='start date for which partitions are to be created in YYYY-MM-DD format')
        parser.add_argument('end_date',  type=str,help='start date for which partitions are to be created in YYYY-MM-DD format')

    def handle(self, *args, **options):
        start_date=options['start_date']
        end_date=options['end_date']

        '''
        Satellite list ideally has to be got from the database
        '''
        satellites=['CARTOSAT_2E','RESOURCESAT_2','RESOURCESAT_2A']

        start_date= datetime. strptime(start_date, '%Y-%m-%d')
        end_date= datetime. strptime(end_date, '%Y-%m-%d')

        partitions={

        }


        day_count = (end_date - start_date).days + 1
        for single_date in (start_date + timedelta(n) for n in range(day_count)):
            
            last_day=calendar.monthrange(single_date.year,single_date.month)[1]
            for sat in satellites:
                part_name=f'geospatial_data_{sat}_{single_date.year}_{single_date.month}'
                part_range=[f'{single_date.year}-{single_date.month}-01',f'{single_date.year}-{single_date.month}-{last_day}']
                partitions[part_name]={
                    'sat':sat,
                    'date_range':part_range
                }
        

            

        '''
        
        DATABASES = {
            'default': {        
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'postgres',
                'USER': 'postgres',
                'PASSWORD': 'gispassword',
                'HOST': 'database',
                'PORT': '5342',
            }
        }
        '''

        database=settings.DATABASES['default']
        DSN=f"user={database['USER']} password={database['PASSWORD']} dbname={database['NAME']} host={database['HOST']} port={database['PORT']}"
        print(DSN)
        with psycopg2.connect(DSN) as conn:
            with conn.cursor() as curs:
                for part in partitions.keys():
                    sat=partitions[part]['sat']
                    date_range=partitions[part]['date_range']
                    query=f"create table if not exists geospatial_data_{sat}  partition of geospatial_data for values in ('{sat}') partition by range(date_of_pass)"
                    curs.execute(query)
                    query=f"create table if not exists {part} partition of geospatial_data_{sat} for values from ('{date_range[0]}') TO ('{date_range[1]}')"
                    curs.execute(query)
            conn.commit()


        