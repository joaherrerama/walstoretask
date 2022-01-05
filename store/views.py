# from django.contrib.gis.db.models.functions import Distance
# from django.contrib.gis.geos import Point

# from django_filters import rest_framework as filters
# from rest_framework import status, viewsets
from rest_framework import viewsets

from .models import PointoOfInterest, Store
from .serializers import POISerializer, StoreSerializer

# from rest_framework.decorators import action
# from rest_framework.response import Response


# from .store_seeker import StoreSeekerFilter


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class PoiViewSet(viewsets.ModelViewSet):
    serializer_class = POISerializer
    queryset = PointoOfInterest.objects.all()
