from django.shortcuts import render
from .models import registration
import random
from django import template
from random import randint
from .models import onlinebus
from .models import seat2
from django.http import HttpResponse

def fun(request):
    return render(request,'profile.html')
def fun1(request):
    if request.method=="POST":
        fullname=request.POST['un']
        password=request.POST['pw']
        email=request.POST['email']
        membership=request.POST['mem']
        mobile=request.POST['mobile']
        s=randint(145662,558963)
        up=registration(fullname=fullname,password=password,email=email,membership=membership,mobile=mobile,userid=s)
        up.save()
        return render(request,'profile.html')
def fun3(request):
    return render(request,'login.html')
def fun4(request):
    if request.method=="POST":
        a=request.POST['fa']
        request.session['name']=request.POST['fa']
        b=request.POST['pwd']
        c=registration.objects.get(fullname__exact=a,password=b)
        return render(request,'success.html',{'us':c})
def fun5(request):
    if request.method=="POST":
        v1=request.POST['su']
        request.session['SOURCE']=request.POST['su']
        v2=request.POST['ds']
        request.session['DESTINATION']=request.POST['ds']
        v3=request.POST['dep']
        request.session['DEPARTURE']=request.POST['dep']
        v4=request.POST['memb']
        if v4=="Premium":
            sp=onlinebus.objects.filter(bustype__exact='AC SEATER',source__exact=v1,destination__exact=v2,departure__exact=v3)
            sp1=onlinebus.objects.filter(bustype__exact='NON-AC SLEEPER',source__exact=v1,destination__exact=v2,departure__exact=v3)
            sp2=onlinebus.objects.filter(bustype__exact='AC MULTI AXLE SEMI SLEEPER',source__exact=v1,destination__exact=v2,departure__exact=v3)
            return render(request,'display.html',{'am':sp,'am1':sp1,'am2':sp2})
        elif v4=="Elite":
            ap=onlinebus.objects.filter(bustype__exact='AC SEATER',source__exact=v1,destination__exact=v2,departure__exact=v3)
            ap1=onlinebus.objects.filter(bustype__exact='AC SLEEPER',source__exact=v1,destination__exact=v2,departure__exact=v3)
            ap2=onlinebus.objects.filter(bustype__exact='AC MULTI AXLE SEMI SLEEPER',source__exact=v1,destination__exact=v2,departure__exact=v3)
            ap3=onlinebus.objects.filter(bustype__exact='NON-AC SLEEPER',source__exact=v1,destination__exact=v2,departure__exact=v3)
            return render(request,'display.html',{'bm':ap,'bm1':ap1,'bm2':ap2,'bm3':ap3})
        elif v4=="Normal":
            lp=onlinebus.objects.filter(bustype__exact='AC SEATER',source__exact=v1,destination__exact=v2,departure__exact=v3)
            lp1=onlinebus.objects.filter(bustype__exact='SUPER LUXERY',source__exact=v1,destination__exact=v2,departure__exact=v3)
            lp2=onlinebus.objects.filter(bustype__exact='DELUXE',source__exact=v1,destination__exact=v2,departure__exact=v3)
            return render(request,'display.html',{'cm':lp,'cm1':lp1,'cm2':lp2})
def fun6(request):
    return render(request,'book.html')
def fun7(request):
    if request.method=="POST":
        ks=request.POST['vehicle1']
        if seat2.objects.filter(seatnumber=ks).exists():
            return HttpResponse("SEAT IS ALLREADY BOOKED")
        else:
            name1=request.session['name']
            name2=request.session['SOURCE']
            name3=request.session['DESTINATION']
            name4=request.session['DEPARTURE']
            ds=seat2(seatnumber=ks,name=name1,SOURCE=name2,DESTINATION=name3,DEPARTURE=name4)
            ds.save()
            ds1=seat2.objects.get(seatnumber=ks)
            return render(request,'bookbus.html',{'mca':ds1})
    return render(request,'book.html')


