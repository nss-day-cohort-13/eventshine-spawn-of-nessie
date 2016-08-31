from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Venue(models.Model):
  # event = models.ForeignKey(Event, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  event_limit = models.BooleanField(default=False)

  def __str__(self):
    return self.name




class Event(models.Model):
  # event_users = models.ForeignKey(EventUser, on_delete = models.CASCADE)
  venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  attendee_limit = models.CharField(max_length=200)


  def get_absolute_url(self):
    return reverse('nessie:index')
  # def __str__(self): #Event.objects.all() now returns a readable string
  #   return self.name, self.description, self.city, self.start_date, self.end_date, self.attendee_limit



class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # is_creator = models.BooleanField(default=False)


# class User(models.Model):
#     event_users = models.ForeignKey(EventUsers, on_delete = models.CASCADE)
#     event = models.ForeignKey(Event, on_delete = models.CASCADE)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)


