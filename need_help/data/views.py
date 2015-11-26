
from django.shortcuts import render
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

        response = 'failure'
    # json_data = json.dumps(response)
    return HttpResponse(response)
    