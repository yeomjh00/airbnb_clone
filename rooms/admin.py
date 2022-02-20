from django.contrib import admin
from . import models

# Register your models here.

# Can register multiple models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """RoomType Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Definition of Admin for Rooms"""

    pass
