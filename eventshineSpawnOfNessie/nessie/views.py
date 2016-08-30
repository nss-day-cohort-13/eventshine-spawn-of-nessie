
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
#whenever you want to make a form to create, update, view a new object
from django.shortcuts import render, redirect
#lets us redirect user on login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#takes username and password, verifies they are a user and they exist in the database
#login attaches session id so user doesnt have to login on every new page you visit
from django.views import generic
from .models import *
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




class Login(generic.TemplateView):

    template_name = 'nessie/login.html'


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    auth = authenticate(username=username, password=password)

    if auth:
        try:
            user = authenticate_user(request, username, password)  # returnsuser object if user is authenticated
            login(request, user)
            return render(request, 'nessie/login.html')
        except:
            return redirect('nessie:index')
    else:
        return redirect('nessie:index')



def authenticate_user(request, username, password):

    user = authenticate(username=username, password=password)

    if user is not None:
        return user
    else:
        return False




def logout_user(request):

    logout(request)

    return redirect('nessie:index')

