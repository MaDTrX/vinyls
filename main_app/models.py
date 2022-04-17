from unicodedata import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


STATE = (
  ('M', 'MINT'),
  ('U', 'USED-zero/little damage'),
  ('S', 'USED-some damage'),
  ('D', 'USED-severe damage'),
)
TYPE = (
  ('O', 'ONLINE'),
  ('p', 'IN-PERSON'),
)
# Create your models here.
class Party(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(
      max_length=1,
      choices = TYPE
      )
    date_time = models.DateField()
    location = models.CharField(max_length=50)

    def __str__(self):
      return  f"{self.name}"

    def get_absolute_url(self):
      return reverse('parties_detail', kwargs={'pk': self.id})

class Vinyl(models.Model):
    title = models.CharField(max_length=100)
    artist =  models.CharField(max_length=100)
    year =  models.IntegerField()
    genre =  models.CharField(max_length=100)
    parties = models.ManyToManyField(Party)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})

class Cleaning(models.Model):
  date = models.DateField('Cleaning Date')
  state = models.CharField(
    max_length=1, 
    choices = STATE,
    default=STATE[0][0]
  )
  vinyl = models.ForeignKey(
    Vinyl, on_delete=models.CASCADE
  )
  def __str__(self):
    return f"{self.get_state_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

def __str__(self):
  return f"Photo for vinyl_id: {self.vinyl_id} @{self.url}"

  



