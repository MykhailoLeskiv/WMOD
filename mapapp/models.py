from django.db import models
from location_field.models.plain import PlainLocationField


# Create your models here.
class Marker(models.Model):
    title = models.CharField(max_length=80)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
