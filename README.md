 # Geospatial CRUD

This project demonstrates simple geospatial crud operations with geodjango. The environment to run the queries and serve the requests is built through docker file. The project is devided into 4 major services.

 1. Core backend service which renders API requests
 2. Data poller , which continuosly polls the countries file online and populates it in the redis broker asynchronously, from which a django mangament command picks it up and pushes it to Database.
 3. Nginx
 4. Redis
 5. Postgis ( postgres along with postgis extension ).

# Docker images for the services

Nginx, Redis and Postgis are configured using their native images where as for the geodjango applicaiton which is the same for backend and the poller, we build it dynamically from the Dockerfile.