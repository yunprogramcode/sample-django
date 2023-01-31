from django.http import HttpResponse
import requests as req

# Create your views here.
def index(request):
	resp = req.request(method='GET', url="http://www.typing.academy")
	print("hello")
	return HttpResponse(resp)