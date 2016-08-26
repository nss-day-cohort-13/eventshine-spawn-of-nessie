from django.db import models

# Create your models here.

class EventUsers(models.Model):
    is_favorite = models.BooleanField(default=False)


class Event(models.Model):
    event_users = models.ForeignKey(EventUsers, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    attendee_limit = models.CharField(max_length=200)


class Venue(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    event_limit = models.BooleanField(default=False)

class User(models.Model):
    event_users = models.ForeignKey(EventUsers, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


