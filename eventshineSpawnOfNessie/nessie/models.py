from django.db import models

# Create your models here.

# class EventUsers(models.Model):
#     is_creator = models.BooleanField(default=False)


class Event(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  attendee_limit = models.CharField(max_length=200)

  def __str__(self): #Event.objects.all() now returns a readable string
    return self.name, self.description, self.city, self.start_date, self.end_date, self.attendee_limit

class Venue(models.Model):
  event = models.ForeignKey(Event, on_delete = models.CASCADE)
  name = models.CharField(max_length=200)
  event_limit = models.BooleanField(default=False)

  def __str__(self):
    return self.name, self.event



# class User(models.Model):
#     event_users = models.ForeignKey(EventUsers, on_delete = models.CASCADE)
#     event = models.ForeignKey(Event, on_delete = models.CASCADE)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)


