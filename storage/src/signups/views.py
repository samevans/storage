from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
# https://docs.djangoproject.com/en/1.11/ref/contrib/messages/
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    
    return render_to_response("home.html", locals(), context_instance=RequestContext(request))

def thankyou(request):
    
    return render_to_response("thankyou.html", locals(), context_instance=RequestContext(request))

def contactus(request):
    
    return render_to_response("contactus.html", locals(), context_instance=RequestContext(request))

def signup(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print form.is_valid(), form.errors, type(form.errors)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            
            messages.success(request, 'We will be in touch')
            messages.info(request, 'WHAT')
            messages.warning(request, 'Your account expires in three days.')
            messages.error(request, 'Document deleted.')
    else:
        form = SignUpForm()
    
    # if form.is_valid():
    #     save_it = form.save(commit=False)
    #     save_it.save()
    #     messages.success(request, 'We will be in touch')
    #     messages.info(request, 'WHAT')
    #     messages.warning(request, 'Your account expires in three days.')
    #     messages.error(request, 'Document deleted.')
    # else:
    #     print form.errors
    #     messages.success(request, 'We will be in touch')
    #     messages.info(request, 'Three credits remain in your account.')
    #     messages.warning(request, 'Your account expires in three days.')
    #     messages.error(request, 'Document deleted.')
    
    
    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))

