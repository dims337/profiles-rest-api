from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """helps djangowork with our custom user model"""

def create_user(self, email, name, password=None):
    """creates a new user profile object."""
    if not email:       #check if email is not blank
        raise ValueError('user must have an email address')

        email = self.normalize_email(email) #standardizes email
        user = self.model(email=email, name=name)

        user.set_password(password) #set psswd which will be encrypted
        user.save(using=self._db) #save in the same database of our project

        return user

def create_superuser(self, email, name, password):
    """creates and saves a new superuser with given details"""
        #function that tells django how to create superusers

        user = self.create_user(email, name, password)


        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)



class Userprofile(AbstractBaseUser, PermissionsMixin):
"""represent a user profile inside our system."""

email = models.EmailField(max_length=255, unique=True)
name = models.charField(max_length=255)
is_active = models.BooleanField(default=True)
is_staff = models.BooleanField(default=False)

objects = UserProfileManager() #object manager to help manage class

USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['name']

def get_full_name(self):
    """used to get a users full name"""

    return self.name


def get_short_name(self):
    """used to get short name"""

    return self.name

def __str__(self):
    """django uses this when it needs to convert the object to a string"""

    return self.email