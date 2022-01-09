from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Country
from . import serializers
from django.db.models import  Subquery
class CountryViewSet(viewsets.ModelViewSet):
    '''

    list (GET request to http://localhost:4000/api/v1/countries/)
    retrieve (GET request to http://localhost:4000/api/v1/countries/{name}/)
    create (POST request to http://localhost:4000/api/v1/countries/)
    update (PUT request to http://localhost:4000/api/v1/countries/{name}/) (it will validate all fields of the model)
    partial update (PATCH request to http://localhost:4000/api/v1/countries/{name}/) (it will run no validation - you can send only fields you've decided to change)
    delete (DELETE request to http://localhost:4000/api/v1/countries/{name}/)

    '''

    # This is a model view set registered under default routers in the global urls file
    # This will automatically create CRUD viewsets for the queryset being returned here
    # The query set here is the list of all countries dynamically evaluated at run time.
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer
    
@api_view(['GET' ])
def match_country_string(request, match):
    '''Example : http://localhost:4000/api/v1/countrymatch/Ind'''

    countries = Country.objects.filter(name__contains=match)
    serializer = serializers.CountrySerializer(countries,many=True)
    return Response(serializer.data)

@api_view(['GET' ])
def intersect_country_area(request, name):
    '''
    Example : http://localhost:4000/api/v1/countryintersect/India

    '''

    intersector=Country.objects.get(name=name)                 
    
    countries=Country.objects.filter(
    scene__intersects=intersector.scene
    )
    
    serializer = serializers.CountrySerializer(countries,many=True)
    return Response(serializer.data)
    
