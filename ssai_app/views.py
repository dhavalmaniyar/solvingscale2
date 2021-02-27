from django.shortcuts import render
from . models import Inquiry,User,UserCount,Snippet
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def company(request):
    return render(request,'company.html')

def consulting(request):
    def get_ip(request):
        address=request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip=address.split(',')[-1].strip()
        else:
            ip=request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=User(user=ip)
    result=User.objects.filter(Q(user__icontains=ip))
    print("EEEEEEEEEEEERRRR",result)
    if len(result)==1:
        print("user exist")
    elif len(result)>1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")
    count=User.objects.all().count()

    datacount=UserCount.objects.get(id=1)
    datacount.ucount=count
    datacount.save()  
    print("count ????????",count)
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


def snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'the detailview for slug of {slug}')

def healthcare(request):
    return render(request,'healthcare.html')

def construction(request):
    return render(request,'construction.html')

def retail(request):
    return render(request,'retail.html')

def automobile(request):
    return render(request,'automobile.html')

def smartcity(request):
    return render(request,'customize.html')