# Geospatial CRUD

This project demonstrates simple geospatial crud operations with geodjango. The environment to run the queries and serve the requests is built through docker file. The project is devided into 4 major services.

 1. Core backend service which renders API requests
 2. Data poller , which continuosly polls the countries file online and populates it in the redis broker asynchronously, from which a django mangament command picks it up and pushes it to Database.
 3. Nginx
 4. Redis
 5. Postgis ( postgres along with postgis extension ).

### Docker images for the services

Nginx, Redis and Postgis are configured using their native images where as for the geodjango applicaiton which is the same for backend and the poller, we build it dynamically from the Dockerfile.


## What is it exactly?

The idea is to demonstrate the running of a geodjango-postgis-redis application using nginx and docker-compose. The country shapes data hosted at this [link](https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json) , is downloaded every 10 minutes and is populated (published) into redis database ( channel : countries.updated ) and all the updates published to redis (countries.* channel) are taken up (subscribed) by a geodjango management command and are populated into the postgis database.

Along with this sample geospatial/non spatial api methods are implemented like , 

 1. ModelViewSet and their routing with default router
 2. Intersecting filter over geometry fields of a postgis table through geodjango ORM.

All these are implemented inside a single image / service termed as backend. This along with other services like postgis/redis/nginx talk through a common bridge network named inside the compose file as django-compose.yml. 

The geodjango applications are currently run through python manage.py runserver command in the debug mode. In production they can be run through gunicorn accordingly without the head of managing any static files because the backend being purely API services.

Finally over this container nginx is run on the djangonetwork to act as a reverse proxy and load balancer. Nginx listens on port 4000 and the django runs on port 8000. 

To spawn the system , the command :

    django-compose up --scale backend=2

Can be used , to spawn 2 containers with backend and nginx forwarding the user requests to those 2 containers by load balancing. ( Actual load balancing is done by docker dns here in the form of  virtualized network )

Host mounts have been used on postgis as docker persistent volumes have a management overhead decreasing the I/O for db ops.

## Steps to spawn the system.

 - Use a preferrably linux & docker installed system 
 - git clone https://github.com/kssvrk/GeospatialCRUD.git to a directory
 - cd GeospatialCRUD
 - Give a system host directory to postgis as the data directory for persistent storage ( under postgis service in docker-compose ).
 - docker-compose up --scale backend=number_of_instances_required
## Sample API end points usage

 - Countries CRUD methods ( Create , retrieve , Update , Destroy ) are implemented under http://localhost:4000/api/v1/countries/ end point. This url will lead to drf api page where examples are shown for all operations.
 - Country search by string match is implemented under http://localhost:4000/api/v1/countrymatch/ end point. Example :
 http://localhost:4000/api/v1/countrymatch/Ind will give India and Indonesia
 - Country intersection by name has been implemented under http://localhost:4000/api/v1/countryintersect/ , appending full name of the country as found in the data will return all the countries intersecting with the named country. Example : http://localhost:4000/api/v1/countryintersect/India will return all the intersecting neighbours of India. 
 

### To Do

 1. Unit tests for the API methods
 2. Load testing for a single container
 3. Production mode settings for geodjango
 4. Non root based dockerfile setup


