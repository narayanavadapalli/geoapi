from django.urls import include, path
from django.contrib import admin
from countries.views import CountryViewSet,match_country_string 
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'countries', CountryViewSet, basename='countries')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls)),
    path('api/v1/',include('countries.urls')),
]