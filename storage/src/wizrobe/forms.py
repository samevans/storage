from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, AuthenticationForm
from models import *

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username','email',)
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserProfile
        fields = ('image','password')


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address

# Config Data
class PersonalSettingsForm(forms.ModelForm):
    class Meta:
        model = PersonalSettings

class ListSpaceOptionsForm(forms.ModelForm):
    class Meta:
        model = ListSpaceOptions      
