from django.urls import path 
from .views import match_country_string,intersect_country_area

urlpatterns = [

    path('countrymatch/<str:match>',match_country_string,name='match_country_string'),
    path('countryintersect/<str:name>',intersect_country_area,name='intersect_country_area')
]
