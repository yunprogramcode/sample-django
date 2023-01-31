from django.http import HttpResponse
import requests as req

def index(request):
  return HttpResponse("Hello world")
