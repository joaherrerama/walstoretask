from rest_framework import status, viewsets
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
            geom=data["geom"],
        )

        new_store.save()

        serializer = StoreSerializer(new_store)

        # Looking Up Code

        poi_list = POILookUp.get_nearby_poi(data["geom"])
        poi_serials = []
        store_id = Store.objects.only("id").get(id=new_store.id)
        for poi in poi_list:
            new_poi = PointoOfInterest.objects.create(
                name=poi["name"],
                bussines_status=poi["bussines_status"],
                rate=poi["rate"],
                type=poi["type"],
                geom=poi["location"],
                store=store_id,
                distance=POILookUp.get_distance(data["geom"], poi["location"]),
            )

            new_poi.save()

            poi_serializer = POISerializer(new_poi)

            poi_serials.append(poi_serializer.data)

        Serializer_list = [serializer.data, poi_list]

        content = {
            "status": 1,
            "responseCode": status.HTTP_200_OK,
            "data": Serializer_list,
        }
        return Response(content)


class PoiViewSet(viewsets.ModelViewSet):
    serializer_class = POISerializer
    queryset = PointoOfInterest.objects.all()
