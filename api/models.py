from django.db import models

class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    class Meta:
        permissions = [
            ("can_view_location", "Can view location"),
            ("can_add_location", "Can add location"),
            ("can_change_location", "Can change location"),
            ("can_delete_location", "Can delete location"),
        ]

    def __str__(self):
        return self.locationName

class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view_item", "Can view item"),
            ("can_add_item", "Can add item"),
            ("can_change_item", "Can change item"),
            ("can_delete_item", "Can delete item"),
        ]

    def __str__(self):
        return self.itemName
