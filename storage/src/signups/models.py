from django.db import models
from django.utils.encoding import smart_unicode

class SignUp(models.Model):
    first_Name = models.CharField(max_length=120, null=False, blank=False)
    last_Name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=120, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.email)
    
    