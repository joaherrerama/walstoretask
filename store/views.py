from rest_framework import viewsets
from rest_framework.response import Response

from .models import PointoOfInterest, Store
from .serializers import POISerializer, StoreSerializer
from .store_seeker import POILookUp

# from rest_framework.decorators import action
# from rest_framework.response import Response


# from .store_seeker import StoreSeekerFilter


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer

    def get_queryset(self):
        stores = Store.objects.all()
        return stores

    def create(self, request, *args, **kwargs):
        data = request.data

        new_store = Store.objects.create(
            name=data["name"],
            address=data["address"],
            city=data["city"],
            postcode=data["postcode"],
            coordinate=data["coordinate"],
        )

        new_store.save()

        serializer = StoreSerializer(new_store)

        # Looking Up Code

        poi_list = POILookUp.get_nearby_poi(data["coordinate"])

        for poi in poi_list:
            new_poi = PointoOfInterest.objects.create(
                name=poi["name"],
                bussines_status=poi["bussines_status"],
                rate=poi["rate"],
                type=poi["type"],
                location=poi["location"],
                store=new_store.id,
                distance=POILookUp.get_distance(data["coordinate"], poi["location"]),
            )

            new_poi.save()

            POISerializer(new_poi)

        return Response(serializer.data)


class PoiViewSet(viewsets.ModelViewSet):
    serializer_class = POISerializer
    queryset = PointoOfInterest.objects.all()
