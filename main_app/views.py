from django.shortcuts import render

# Create your views here.
#! dont forget to import HttpResponse
from django.http  import HttpResponse

class Vinyl:
    def __init__(self, title, artist, year, genre):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre

vinyls = [
    Vinyl('To pimp a butterfly','Kendrick Lamar','2015','Hip-hop'),
    Vinyl('My beatiful twisted dark fantasy','Ye','2010','Hip-hop'),
    Vinyl('American Dream','LCD sound system','2017','Rock'),
    Vinyl('Discovery','Daft Punk','2001','Electronic')
]

#Define the home view
def home(request):
    return render(request, 'home.html')

#Define the about view
def about(request):
    return render(request,'about.html')

#Define the vinyle index
def vinyls_index(request):
    return render(request, 'vinyls/index.html',  {'vinyls': vinyls})