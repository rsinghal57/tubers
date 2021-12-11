from django.shortcuts import render, redirect
from .models import Slider,Team
from hiretubers.models import Contactteam
from youtubers.models import Youtuber
from django.contrib import messages

# Create your views here.

def home(request):
    sliders=Slider.objects.all()
    teams=Team.objects.all()
    featured_youtubers=Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers=Youtuber.objects.all().order_by('-created_date')
    data={
        'sliders':sliders,
        'teams':teams,
        'featured_youtubers':featured_youtubers,
        'all_youtubers':all_youtubers
    }
    return render(request,'webpages/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        "teams":teams
    }
    return render(request,'webpages/about.html',data)

def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        company=request.POST['company']
        phone=request.POST['phone']
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']
        
        contactteam=Contactteam(name=name, company=company, phone=phone, email=email,subject=subject, message=message)
        contactteam.save()
        messages.success(request,'Thanks for reaching out!')
        return redirect('contact')

    return render(request,'webpages/contact.html')