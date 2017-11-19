from django import forms
from .models import LogIn, SignUp

class LoginForm(forms.ModelForm):
    class Meta:
        model = LogIn
	   
class SignupForm(forms.ModelForm):
    class Meta:
        model = SignUp
