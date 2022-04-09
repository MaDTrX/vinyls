from django.shortcuts import render

# Create your views here.
#! dont forget to import HttpResponse
from django.http  import HttpResponse


#Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

#Define the about view
def about(request):
    return render(request,'about.html')

#Define the about index
def vinyl_index(request):
    return render(request, 'vinyls/index.html',  {'vinyls': vinyls })