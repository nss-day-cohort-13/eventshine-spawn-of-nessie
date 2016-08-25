from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Venue, User


def index(request):
    # all_events = Event.objects.all()
    return HttpResponse("Hello, world. You're at the nessie event index.")

