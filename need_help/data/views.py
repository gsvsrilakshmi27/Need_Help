
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
    response = {}
    if not Donor.objects.filter(donar_name=donar_name):
        s = Donor(donar_name=donar_name, blood_group=blood_group, city_name = city, mobile_number = mobile_number,password= password)
        s.save()
        response['status'] = 'sucess'
    else:
        response['status'] = 'failure'
    json_data = json.dumps(response)
    return HttpResponse(json_data, content_type = "application/json")