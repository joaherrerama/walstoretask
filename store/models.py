from django.contrib.gis.db import models


class Store(models.Model):
    """
    A model which holds information about a particular store
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postcode = models.IntegerField()
    geom = models.PointField()

    class Meta:
        managed = True
        db_table = "store_table"


class PointoOfInterest(models.Model):
    """
    A model which holds information about a POI from Google maps Lookup
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bussines_status = models.CharField(max_length=255)
    rate = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    geom = models.PointField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "poi_table"
