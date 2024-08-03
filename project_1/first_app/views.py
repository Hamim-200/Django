from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.

def courses(request):
    return HttpResponse("This is courses pageeee")

def about(request):
    return HttpResponse("This is first app about pageeee")

def home(request):
    return HttpResponse("This is first app HOME pageeee")