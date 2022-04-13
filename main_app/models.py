from django.db import models
from django.urls import reverse


TIME = (
  ('E', 'Evening'),
  ('N', 'Night'),
  ('A', 'After-Hours'),
)
# Create your models here.
class Vinyl(models.Model):
    title = models.CharField(max_length=100)
    artist =  models.CharField(max_length=100)
    year =  models.IntegerField()
    genre =  models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})

class Party(models.Model):
  date = models.DateField('Party Date')
  time = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=TIME,
    # set the default to be 'B'
    default=TIME[0][0]
  )
  # creates a cat_id column
  vinyl = models.ForeignKey(
    Vinyl,
    # automatically delete all feedings with the cat
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

