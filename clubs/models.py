from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Member(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name=models.CharField(max_length=50, blank = False)
    last_name=models.CharField(max_length=50, blank = False)
    email = models.EmailField(unique=True, blank=False)
    bio = models.CharField(max_length=520, blank=True)
    experience_level = models.IntegerField(
        default=3,
        unique=False,
        validators= [MinValueValidator(1),MaxValueValidator(6)]
    )
    personal_statement = models.CharField(max_length=520, blank=True)
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
