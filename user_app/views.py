from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerRegisterationForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=="POST":
        register_form=CustomerRegisterationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New user Added. Login to enter."))
            return redirect('register')
    else:
        register_form=CustomerRegisterationForm()
    return render(request,'register.html',{'register_form':register_form})