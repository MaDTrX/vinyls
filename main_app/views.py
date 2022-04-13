from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vinyl
from .forms import ListeningForm

#Define the home view
def home(request):
    return render(request, 'home.html')

#Define the about view
def about(request):
    return render(request,'about.html')

#Define the vinyle index
def vinyls_index(request):
  vinyls = Vinyl.objects.all()
  return render(request, 'vinyls/index.html', { 'vinyls': vinyls })

def vinyls_detail(request, vinyl_id):
  vinyl = Vinyl.objects.get(id=vinyl_id)
  listening_form = ListeningForm()
  return render(request, 'vinyls/detail.html', { 'vinyl': vinyl, 'listening_form': listening_form })
  
class VinylCreate(CreateView):
  model = Vinyl
  fields = '__all__'

class VinylUpdate(UpdateView):
  model = Vinyl
  fields = ['title', 'artist', 'year']

class VinylDelete(DeleteView):
  model = Vinyl
  success_url = '/vinyls/'


def add_feeding(request, vinyl_id):
  # create a ModelForm instance using the data in the posted form
  form = FeedingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.vinyl_id = vinyl_id
    new_feeding.save()
  return redirect('detail', vinyl_id=vinyl_id)