from django.shortcuts import render
from django.http import HttpResponse
from Backend.Auth.views import *
from Backend.Auth.models import *

def index(request):
	return HttpResponse('Hello from the index page')