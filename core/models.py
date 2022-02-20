from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """Time Stamped Model"""

    # auto_now_add = True: When the object is created, the date will be set to the current date and time.
    # auto_now = True: When the object is saved, the date will be set to the current date and time.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
