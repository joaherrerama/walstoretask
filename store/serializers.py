from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import PointoOfInterest, Store


class StoreSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"
        geo_field = "geom"


class POISerializer(GeoFeatureModelSerializer):

    distance = serializers.CharField()

    class Meta:
        model = PointoOfInterest
        fields = "__all__"
        geo_field = "geom"
        read_only_fields = ["distance"]
