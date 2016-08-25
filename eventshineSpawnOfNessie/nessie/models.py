from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    start_date = models.DateTimeField('date started')
    end_date = models.DateTimeField('date ended')
    attendee_limit = models.CharField(max_length=200)

class Venue(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    event_limit = models.CharField(max_length=200)

class User(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

