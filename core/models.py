#To generate uuid and os for file path management functions 
import uuid
import os

from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser,
BaseUserManager,
PermissionsMixin
)

from django.conf import settings

#Function for to generate a path for image upload
def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = os.path.splitext(filename)[1]
    # ext = filename.split('.')[-1] #from git
    filename = f'{uuid.uuid4()}.{ext}' 

    # return os.path.join('uploads/recipe/', filename) #from git
    return os.path.join('uploads','recipe', filename)

# ***********************************************************
#**extra_fields - can provide any number of keyword arguments ,
#it means if we create any fileds in user class no need to update here again and again  
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

# AbstractBaseUser - functionlaity for auth system 
# PermissionsMixin - Functionality for the permissions and fields
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #login with django admin

    objects = UserManager() #Assign above UserManager to this custom user class 

    USERNAME_FIELD = 'email'

class Recipe(models.Model):
    """Recipe"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2,default='0')
    link = models.CharField(max_length=255, blank=True,default='http://go.com')
    description =  models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField('Tag')  #many to many relation
    ingredients = models.ManyToManyField('Ingredient')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    """Tag"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """Ingredient"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Employee(models.Model):
    """Employee"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    empName = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    empAddress = models.CharField(max_length=255)
    department = models.CharField(max_length=10)

