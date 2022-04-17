from django.forms import ModelForm
from .models import Cleaning, Party

class CleaningForm(ModelForm):
  class Meta:
    model = Cleaning
    fields = ['date', 'state']
