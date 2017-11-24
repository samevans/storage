from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User)
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
    profile = models.CharField(max_length=120, default='')
    account = models.CharField(max_length=120, default='')
    billing = models.CharField(max_length=120, default='')
