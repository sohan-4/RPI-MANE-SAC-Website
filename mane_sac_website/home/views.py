from django.shortcuts import render
from .models import *

# Create your views here.

def home_view(request):
    events = event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'home/home.html', context)

def about_view(request):
    info = about.objects.all()
    context = {
        'info': info
    }
    return render(request, 'home/about.html', context)

def member_view(request):
    return render(request, 'home/members.html')

def contact_view(request):
    return render(request, 'home/contact.html')

def faq_view(request):
    return render(request, 'home/faq.html')