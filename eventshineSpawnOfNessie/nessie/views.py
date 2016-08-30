
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
#whenever you want to make a form to create, update, view a new object
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
#lets us redirect user on login
from django.contrib.auth import authenticate, login, logout

#takes username and password, verifies they are a user and they exist in the database
#login attaches session id so user doesnt have to login on every new page you visit
from django.views import generic
from django.views.generic import View
from .models import Event, Venue
from django.contrib.auth.models import User

class IndexView(generic.ListView):
  template_name = 'nessie/index.html'
  context_object_name = 'all_events'

  def get_queryset(self):
    return Event.objects.all()

class EventCreate(CreateView):
  model = Event
  fields = ['name', 'description', 'city', 'start_date', 'end_date', 'attendee_limit']

class Register(generic.TemplateView):

  template_name='nessie/register_user.html'

def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    user = User.objects.create_user(username=username, password=password,
                                    email=email)

    user.save()
    return redirect('nessie:index')


def authenticate_user(request, username, password):

    user = authenticate(username=userName, password=passWord)

    if user is not None:
        return user
    else:
        return False



def logout_user(request):

    logout(request)

    return redirect('nessie:index')
