from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"store", views.StoreViewSet, basename="store")
router.register(r"poi", views.PoiViewSet, basename="poi")

urlpatterns = [
    path("", include(router.urls)),
    path("stores/", include("rest_framework.urls", namespace="rest_framework")),
]
