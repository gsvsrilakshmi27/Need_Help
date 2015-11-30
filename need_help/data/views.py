
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import Donor
import cgi
import os
import json
from django.conf import settings
from django.template import RequestContext, loader


# Create your views here.
def index(request):
    return render(request, "data/index.html")

def registration(request):
    return render(request,"data/registration.html")

# def retrieval(request):
    # Donor_list=Donor.objects.all()
    # template = loader.get_template('data/retrieval.html')
    # context = RequestContext(request, {
    #            'Donor_details': Donor_list
    # })
    # return HttpResponse(template.render(context))
    # return render(request,"data/retrieval.html")
def validate(request):

    """return HttpResponse("Hello, world. You're at the polls index.")"""
    donar_name = request.GET.get('donar_name')
    blood_group = request.GET.get('blood_group')
    mobile_number = request.GET.get('mobile_number')
    city = request.GET.get('city')
    password = request.GET.get('password')
    password1 = request.GET.get('password1')
    response = {}
   
    if blood_group == 'Select blood group':
        response = 'select any blood group'
        return HttpResponse(response)

    if not int(mobile_number) >= 7000000000 and int(mobile_number) <= 9999999999:
        response = 'enter valid mobile number'
        return HttpResponse(response)

    if city == 'Select city':
        response = 'select any city'
        return HttpResponse(response)

    if not password == password1:
        response = 'password missmatch'
        return HttpResponse(response)

    if not Donor.objects.filter(mobile_number = mobile_number):
        s = Donor(donar_name=donar_name, blood_group=blood_group, city_name = city, mobile_number = mobile_number,password= password)
        s.save()
        response = 'sucess'
    else:

        response = 'already registered'
    # json_data = json.dumps(response)
    return HttpResponse(response)

def validate1(request):
    
    """return HttpResponse("Hello, world. You're at the polls index.")"""
    mob_num = request.POST.get('MobileNumber')
    pwd = request.POST.get('Password')
   
    if Donor.objects.filter(mobile_number = mob_num,password=pwd):
        return render_to_response(
              'data/login.html',
            )
    else:
        return render_to_response(
              'data/alert.html',
            )


def validate2(request):
    """return HttpResponse("Hello, world. You're at the polls index.")"""
    phone = request.GET.get('phonenumber')
    pwd = request.GET.get('oldpassword')
    pwd1 = request.GET.get('newpassword')
    pwd2 = request.GET.get('renewpassword')

    response = {}
    if not pwd1 == pwd2:
        response = 'new password mismatch'
        return HttpResponse(response)


    if Donor.objects.filter(mobile_number=phone,password = pwd):
        Donor.objects.filter(mobile_number=phone).update(password=pwd1)
        # s.save()
        response = 'password changed'
        return HttpResponse(response)

    else:
        response = 'enter old mobile number and password correctly'
        return HttpResponse(response)

def validate3(request):

    """return HttpResponse("Hello, world. You're at the polls index.")"""
    
    mob = request.GET.get('oldmobile')
    mob1 = request.GET.get('newmobile')
    mob2 = request.GET.get('renewmobile')

    response = {}
    if not int(mob1) == int(mob2):
        response = 'new phonenumber mismatch'
        return HttpResponse(response)

    if not int(mob1) >= 7000000000 and int(mob1) <= 9999999999:
        response = 'enter valid mobile number'
        return HttpResponse(response)

    if Donor.objects.filter(mobile_number=mob):
        Donor.objects.filter(mobile_number=mob).update(mobile_number=mob1)
        # s.save()
        response = 'password changed'
        return HttpResponse(response)
    else:
        response = 'enter old mobile number correctly'
        return HttpResponse(response)
        
def validate4(request):
    requiredcity= request.GET.get('cit')
    requiredbloodgroup = request.GET.get('blod')
    if requiredcity == 'city' or requiredbloodgroup == 'Select blood group':
        return render_to_response(
              'data/alert1.html',
            )
    else:
        Donor_list=Donor.objects.filter(city_name = requiredcity,blood_group = requiredbloodgroup )
        template = loader.get_template('data/retrieval.html')
        context = RequestContext(request, {
        'Donor_details': Donor_list
        })
        return HttpResponse(template.render(context))



    


    