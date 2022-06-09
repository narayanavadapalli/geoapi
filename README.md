# SEARCH MICRO

This project is a ongoing project under bhoonidhi to develop a search service for the satellite data.

This project uses the concept of Partitions to distribute the huge repository of satellite
data into different pieces and there by using a single placeholder table for all the operations
instead of  doing complex joins and repeated index creation. This will allow postgres engine
to build query plans which are smart based on the usage / data statistics.

We use POSTGIS here as a spatial database with a polygon column and a json field to hold all other non essential metadata.

