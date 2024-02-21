from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class PointOfInterest(models.Model):
    poi_id = models.AutoField(primary_key=True)
    poi_external_id = models.CharField(max_length=255)
    poi_name = models.CharField(max_length=255)
    poi_latitude = models.FloatField()
    poi_longitude = models.FloatField()
    poi_category = models.CharField(max_length=255)
    poi_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.poi_name


class Rating(models.Model):
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE, related_name='ratings')
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
