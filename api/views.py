from rest_framework import viewsets
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer
from .permissions import ModelPermissionsByMethod  # Import the custom permission class

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [ModelPermissionsByMethod]  # Apply the custom permission class

    def get_queryset(self):
        queryset = super().get_queryset()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        return queryset

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [ModelPermissionsByMethod]  # Apply the custom permission class
