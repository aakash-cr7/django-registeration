from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Set'),
)

'''
    Custom user class for user registerations. Add all the desired properties here
'''
class CustomUser(AbstractUser):
    gender = models.CharField(max_length = 2, choices = GENDER_CHOICES, default = GENDER_CHOICES[2][0])

    class Meta:
        unique_together = ('email',)
        verbose_name = 'User'

