# from locale import currency
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # Docstring below
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_USD = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_USD, "KRW"))

    # ImageField need module "Pillow"
    avatar = models.ImageField(blank=True)
    # CharField need One argument, max_length
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)

    bio = models.TextField(default="", blank=True)
