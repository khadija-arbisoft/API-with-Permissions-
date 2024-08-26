from rest_framework import serializers
from .models import Item, Location

class ItemSerializer(serializers.Serializer):
    itemName = serializers.CharField(max_length=100)
    date_added = serializers.DateField()
    itemLocation = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.itemName = validated_data.get('itemName', instance.itemName)
        instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.itemLocation = validated_data.get('itemLocation', instance.itemLocation)
        instance.save()
        return instance

class LocationSerializer(serializers.Serializer):
    locationName = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.locationName = validated_data.get('locationName', instance.locationName)
        instance.save()
        return instance

class ItemListSerializer(serializers.ListSerializer):
    child = ItemSerializer()

class LocationListSerializer(serializers.ListSerializer):
    child = LocationSerializer()
