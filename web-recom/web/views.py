from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *


def search(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            messages.success(request ,'sent' ,'success')
            return redirect ('home')
        
    else:
        form = UsernameForm()
    return render(request ,'search.html' , {'form':form})



def home(request):
    return render(request , 'home.html')

