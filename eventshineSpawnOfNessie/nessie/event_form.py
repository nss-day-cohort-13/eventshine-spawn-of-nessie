from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.forms import Textarea, CheckboxInput, DateInput
from .models import Event

# form used to create and edit a post
class CreateForm(forms.ModelForm):
  class Meta:
    model = Event

      fields = [
        "title",
        "description",
        "location",
        "start_date",
        "end_date",
        "attendee_limit",
        "venue"
        ]
      widgets = {
        # this sets the input text area
        "description": forms.Textarea(attrs={"cols": 60, "rows": 30}),
        "start_date": forms.TextInput(attrs={'placeholder': 'dd/mm/yy 5:30 PM'})
        "end_date": forms.TextInput(attrs={'placeholder': 'dd/mm/yy 7:30 PM'})
        }