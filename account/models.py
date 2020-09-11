from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    dog_name = models.CharField(max_length=20,null=True)
    dog_gender = models.CharField(max_length=20,null=True)
    dog_type = models.CharField(max_length=20, null=True)
    dog_birth_year = models.IntegerField(null=True, blank=True)
    dog_birth_month = models.IntegerField(null=True, blank=True)
    dog_birth_day = models.IntegerField(null=True, blank=True)
    dog_Image = models.ImageField(null=True)
