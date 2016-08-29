
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
from .forms import UserForm


class IndexView(generic.ListView):
  template_name = 'nessie/index.html'
  context_object_name = 'all_events'

  def get_queryset(self):
    return Event.objects.all()

class EventCreate(CreateView):
  model = Event
  fields = ['name', 'description', 'city', 'start_date', 'end_date', 'attendee_limit']


class UserFormView(View):
  form_class = UserForm
  template_name = 'nessie/registration_form.html'

  #display blank form for new user
  def get(self, request):
    #use this form (userform)
    form = self.form_class(None)
    return render(request, self.template_name, {'form' : form})
  #process form data
  def post(self,request):
    form = self.form_class(request.POST)


  #creates user object from form but does not store in database
    if form.is_valid():
      #
      user=form.save(commit=False)

      #cleaned(normalzed) data - ensures data is always formatted proper
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      # user.set_password(password)
      #gives you ability to change user password
      user.save()

      #returns User objects if user exists
      user = authenticate(username=username, password=password)

      if user is not None:
        if user.is_active:
          #actually logs in user and attaches user to session
          login(request, user)
          #retuns user to index if user logs in successfully
          return redirect('nessie:index')

    #if not reload form
    return render(request, self.template_name, {'form' : form})


