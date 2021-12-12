from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(AbstractUser):
    username = None
    first_name=models.CharField(max_length=50, blank = False)
    last_name=models.CharField(max_length=50, blank = False)
    email = models.EmailField(unique=True, blank=False)
    bio = models.CharField(max_length=520, blank=True)
    EXPERIENCE_LEVEL_CHOICES = (
      (1, 'Novice'),
      (2, 'Beginner'),
      (3, 'Intermediate'),
      (4, 'Advanced'),
      (5, 'Expert'),
    )
    experience_level = models.PositiveSmallIntegerField(choices=EXPERIENCE_LEVEL_CHOICES, default=2)
    personal_statement = models.CharField(max_length=520, blank=True)
    USER_TYPE_CHOICES = (
      (1, 'Applicant'),
      (2, 'Member'),
      (3, 'Officer'),
      (4, 'Owner'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []