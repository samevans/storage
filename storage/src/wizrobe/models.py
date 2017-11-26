from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from PIL import Image
from base.constants import *

# class UserProfileManager(models.Manager):
#      def get_queryset(self):
#          return super(UserProfileManager, self).get_queryset().filter(phone=123)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=120, default='', blank=True)
    zipcode = models.CharField(max_length=120, default='', blank=True)
    city = models.CharField(max_length=120, default='', blank=True)
    phone = models.IntegerField(default=0, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    
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

# DataConfig
class PersonalSettings(models.Model):
    profile = models.CharField(max_length=120, default='', help_text='/'+SETTINGS_PROFILE_URL)
    account = models.CharField(max_length=120, default='', help_text='/'+SETTINGS_ACCOUNT_URL)
    billing = models.CharField(max_length=120, default='', help_text='')
    emails = models.CharField(max_length=120, default='', help_text='')
