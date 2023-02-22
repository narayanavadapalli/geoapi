from django.contrib.gis.db import models

class Country(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    scene = models.MultiPolygonField(null=False,blank=False)
    
    def __str__(self):
        return f"{self.name}"
