from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User, AnonymousUser
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import *
from .models import *
from base.constants import *

def home(request):
    args = {'request':request}
    if request.user.is_authenticated is not AnonymousUser:
        args['user'] = request.user
    
    return render(request, 'home.html', args)


@login_required(login_url='/login')
def dashboard(request):
    args = {'request':request}
    if request.user.is_authenticated is not AnonymousUser:
        args['user'] = request.user
    
    return render(request, 'dashboard.html', args)


def contactus(request):
    args = {'request':request}
    if request.user.is_authenticated is not AnonymousUser:
        args['user'] = request.user
    
    return render(request, 'contactus.html', args)


@login_required(login_url='/login')
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            save_signup = form.save(commit=False)
            save_signup.save()
            
            if settings.EMAILS_ON:
                subject = 'Create account validation'
                message = 'Welcome to Wizrobe.'
                from_email = settings.EMAIL_HOST_USER
                to_list = [save_signup.email, settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            messages.success(request, 'We have received your request. Please validate through your email.')
            return HttpResponseRedirect('/login')
        else:
            print form.is_valid(), form.errors, type(form.errors)
    else:
        form = RegistrationForm()
        
    args = {'form': form, 'request': request}

    return render(request, 'signup.html', args)


@login_required(login_url='/login')
def view_profile(request):
    args = { 'user': request.user, 'request': request }
    return render(request, 'profile.html', args)


@login_required(login_url='/login')
def settings_profile(request):
    if request.method == 'POST':
        
        # get primarykey for user
        _user = UserProfile.objects.filter(user=request.user)
        _userid = _user.values_list('user_id', flat=True).distinct()
        u = UserProfile.objects.get(pk=_userid[0])
        
        if 'POSTprofilepic' in request.POST:
            form = UserChangeForm(request.POST, request.FILES)
            if form.is_valid():
                u.image = form.cleaned_data['image']
                u.save()
                
        elif 'POSTbasicinfo' in request.POST:
            form = UserChangeForm(request.POST)
            if form.is_valid():
                # u.zipcode = form.cleaned_data['zipcode']
                u.save()
                
        return HttpResponseRedirect('/settings/profile')
        # return HttpResponseRedirect('/profile')       
            
    form = UserChangeForm(instance=request.user.userprofile)
    
    args = { 'form':form, 'request':request, 'settings':PersonalSettingsForm() }
    return render(request, 'settings_profile.html', args)


@login_required(login_url='/login')
def settings_account(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/settings/account')
            
    else:
        form = PasswordChangeForm(user=request.user)
    
    args = { 'form':form, 'request':request , 'settings':PersonalSettingsForm()}
    return render(request, 'settings_account.html', args)


@login_required(login_url='/login')
def successfully_loggedin(request):
    # return HttpResponseRedirect('/profile')
    return HttpResponseRedirect('/dashboard')
    
    
@login_required(login_url='/login')
def listing(request):
    return HttpResponseRedirect('/'+LISTINGS_LOCATION)
    

@login_required(login_url='/login')
def listing_location(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    else:
        form = AddressForm(initial={'state':''})
        
    args = {
        'request':request,
        'form':form,
        'listingoptions': ListSpaceOptionsForm(),
        'states': US_STATES_DICT
    }
    return render(request, 'listing_address.html', args)