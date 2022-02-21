from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    # First, insert component of Web Application
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField
    check_in = models.IntegerField()
    value = models.IntegerField()

    # Second, insert Foreign Key
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"
