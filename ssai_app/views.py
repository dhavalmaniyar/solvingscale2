from django.shortcuts import render
from . models import Inquiry
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request,'index.html')

def company(request):
    return render(request,'company.html')

def consulting(request):
    return render(request,'consulting.html')

def portfolio(request):
    return render(request,'portfolio.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')


def submit(request):
    name=request.POST['name']
    mobile=request.POST['mobile']
    email=request.POST['email']
    inquiry=request.POST['inquiry']
    pay=request.POST['pay']
    need=request.POST['need']
    data=Inquiry(name=name,mobile=mobile,email=email,inquiry=inquiry,pay=pay,need=need)
    data.save()
    subject = 'Free Consultation Inquiry'
    message = 'name: '+name+'\nmobile: '+mobile+'\nemail: '+email+'\nInquiry: '+inquiry+'\nReady to Pay: '+pay+'\nRequirements: '+need
    send_mail(subject, 
            message,'infosolvingscale@gmail.com', ['infosolvingscale@gmail.com'], fail_silently = False)
    return render(request,'consulting.html',{'message':"Thank You, we will contact you soon"})