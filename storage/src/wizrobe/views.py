from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import RegistrationForm

def home(request):
    return render_to_response("home.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/login')
def dashboard(request):
    
    print request.user
    
    return render_to_response("dashboard.html", locals(), context_instance=RequestContext(request))

def contactus(request):
    return render_to_response("contactus.html", locals(), context_instance=RequestContext(request))


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
            
            # for now I am just going to validate user automatically
            # user = User.objects.create_user(save_signup.email, save_signup.email, save_signup.password)
            # print '1'
            # user.save()
            
            messages.success(request, 'We have received your request. Please validate through your email.')
            return HttpResponseRedirect('/login')
        else:
            print form.is_valid(), form.errors, type(form.errors)
    else:
        form = RegistrationForm()
    
    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))


def requestpassword(request):
    return render_to_response("requestpassword.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/login')
def view_profile(request):
    return render_to_response("profile.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/login')
def edit_profile(request):
    return render_to_response("profile_edit.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/login')
def goto_dashboard(request):
    return HttpResponseRedirect('/dashboard')