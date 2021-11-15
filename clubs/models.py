from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    first_name=models.CharField(max_length=50, blank = False)
    last_name=models.CharField(max_length=50, blank = False)
    email = models.EmailField(unique=True, blank=False)
    bio = models.CharField(max_length=520, blank=True)
    novice = 6
    beginner = 5
    intermediate = 4
    intermediate2 = 3
    advanced = 2
    expert = 1
    level_choices = (
        (novice, 'Novice'),
        (beginner, 'Beginner'),
        (intermediate, 'Intermediate'),
        (intermediate2, 'Intermediate2'),
        (advanced, 'Advanced'),
        (expert, 'Expert'),
    )
    experience_level = models.IntegerField(choices=level_choices, blank=False, null=False)
    personal_statement = models.CharField(max_length=520, blank=True)
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
