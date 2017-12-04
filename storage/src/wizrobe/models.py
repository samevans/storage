from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from PIL import Image
from base.constants import *


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=120, default='', blank=False)
    city = models.CharField(max_length=120, default='', blank=False)
    state = models.CharField(max_length=120, choices=US_STATES, default='', blank=False)
    zip_code = models.CharField(max_length=12, default='', blank=False)
    hide_address = models.BooleanField(default=False)
    
    def __str__(self):
        return self.street_address + ', ' + self.city + ', ' + self.state + ' ' + self.zip_code
    
  
    
class UserProfile(models.Model):
    user =    models.OneToOneField(User)
    name =    models.CharField(max_length=120, default='', blank=True)
    image =   models.ImageField(upload_to='profile_image', blank=True)
    
    def __str__(self):
        return self.user.username
    
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/assets/defaultprofile.jpg'
    
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
            
post_save.connect(create_profile, sender=User)

    
    
    
class Space(models.Model):
    ROOM = 'RM'
    DRIVEWAY = 'DR'
    CLOSET = 'CL'
    SHELF = 'SH'
    WIZROBE_CHOICES = (
        (ROOM, 'Room'),
        (CLOSET, 'Closet'),
        (SHELF, 'Shelf'),
        (DRIVEWAY, 'Driveway'),
    )
    lister =              models.OneToOneField(User)
    address =             models.OneToOneField(Address)
    
    title =               models.CharField(max_length=120, default='', blank=False)
    dimensions =          models.CharField(max_length=120, default='', blank=True)
    location =            models.CharField(max_length=120, default='', blank=True)
    type_of_storage =     models.CharField(max_length=2,choices=WIZROBE_CHOICES,default=ROOM,blank=False)
    available_from =      models.DateField(blank=False)#auto_now=True, 
    available_to =        models.DateField()
    price =               models.CharField(max_length=120, default='', blank=False)
    image =               models.ImageField(upload_to='spaces', blank=True)
    
    def __str__(self):
        return self.title
    
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/assets/defaultprofile.jpg'




# Configuration Data
################################################################################################
class ListSpaceOptions(models.Model):
    location =         models.CharField(max_length=120, default='', help_text='/'+LISTINGS_LOCATION)
    contact_info =     models.CharField(max_length=120, default='', help_text='/'+LISTINGS_LOCATION)
    basic_details =    models.CharField(max_length=120, default='', help_text='/'+LISTINGS_LOCATION)
    photos_and_video = models.CharField(max_length=120, default='', help_text='/'+LISTINGS_LOCATION)
    description =      models.CharField(max_length=120, default='', help_text='/'+LISTINGS_LOCATION)
    review =           models.CharField(max_length=120, default='', help_text='/'+LISTINGS_LOCATION)


class PersonalSettings(models.Model):
    profile = models.CharField(max_length=120, default='', help_text='/'+SETTINGS_PROFILE_URL)
    account = models.CharField(max_length=120, default='', help_text='/'+SETTINGS_ACCOUNT_URL)
    billing = models.CharField(max_length=120, default='', help_text='')
    emails =  models.CharField(max_length=120, default='', help_text='')
