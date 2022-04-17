from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CleaningForm
import os
import uuid
import boto3
from .models import Party, Vinyl, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def some_function(request):
  secret_key = os.environ['SECRET_KEY']

#Define the home view
def home(request):
    return render(request, 'home.html')

#Define the about view
def about(request):
    return render(request,'about.html')

#Define the vinyle index
@login_required
def vinyls_index(request):
  vinyls = Vinyl.objects.all()
  return render(request, 'vinyls/index.html', { 'vinyls': vinyls })

def vinyls_detail(request, vinyl_id):
  vinyl = Vinyl.objects.get(id=vinyl_id)
  cleaning_form = CleaningForm()
  not_included = Party.objects.exclude(id__in=vinyl.parties.all().values_list('id')) 
  return render(request, 'vinyls/detail.html', { 'vinyl': vinyl, 'cleaning_form': cleaning_form, 'partys': not_included })

def add_photo(request, vinyl_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to vinyl_id or vinyl (if you have a vinyl object)
            print(url)
            Photo.objects.create(url=url, vinyl_id=vinyl_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', vinyl_id=vinyl_id)


class VinylCreate(CreateView):
  model = Vinyl
  fields = '__all__'
  success_url = '/vinyls/'

class VinylUpdate(UpdateView):
  model = Vinyl
  fields = ['title', 'artist', 'year']

class VinylDelete(DeleteView):
  model = Vinyl
  success_url = '/vinyls/'


def add_cleaning(request, vinyl_id):
  # create a ModelForm instance using the data in the posted form
  form = CleaningForm(request.POST)
  # validate the data
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.vinyl_id = vinyl_id
    new_cleaning.save()
  return redirect('detail', vinyl_id=vinyl_id)

class PartyList(ListView):
  model = Party
  template_name = 'parties/index.html'

class PartyDetail(DetailView):
  model = Party
  
class PartyCreate(CreateView):
  model = Party
  fields = '__all__'
  success_url = '/parties/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class PartyUpdate(UpdateView):
  model = Party
  fields = '__all__'
  success_url = '/parties/'
  
class PartyDelete(DeleteView):
  model = Party
  fields = '__all__'
  success_url = '/parties/'

def assoc_party(request, vinyl_id, party_id):
  Vinyl.objects.get(id=vinyl_id).parties.add(party_id)
  return redirect('detail', vinyl_id=vinyl_id)

def unassoc_party(request, vinyl_id, party_id):
  Vinyl.objects.get(id=vinyl_id).parties.remove(party_id)
  return redirect('detail', vinyl_id=vinyl_id)

