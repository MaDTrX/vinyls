from django.shortcuts import render

# Create your views here.
#! dont forget to import HttpResponse
from django.http  import HttpResponse


#Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

#Define the about view
def about(request):
    return HttpResponse('<h1>About</h1>')

#Define the about index
def index(request):
    return HttpResponse('<h1>Vinyls</h1>')