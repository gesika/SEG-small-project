from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email,password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email = email,
                            is_staff = is_staff,
                            is_superuser = is_superuser,
                            last_login = now,
                            date_joined = now,
                            **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        user = self._create_user(email, password, False, False, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user


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
    experience_level = models.PositiveSmallIntegerField(choices=EXPERIENCE_LEVEL_CHOICES)
    personal_statement = models.CharField(max_length=520, blank=True)
    USER_TYPE_CHOICES = (
      (1, 'Applicant'),
      (2, 'Member'),
      (3, 'Officer'),
      (4, 'Owner'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    
    """class Types(models.TextChoices):
        Applicant = "Applicant"
        Member = "Member"
        Officer = "Officer"
        Owner = "Owner" 
        
    default_type = Types.Member
        
    type = models.CharField(max_length=255, choices=Types.choices, default=default_type)"""
    
    objects = UserManager()
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the email."""
        return self.email

    def get_short_name(self):
        """Return the email."""
        return self.email