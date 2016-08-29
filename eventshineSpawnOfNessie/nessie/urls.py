from django.conf.urls import url
from . import views
app_name = 'nessie'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'event/add$', views.EventCreate.as_view(), name='event_add'),
]
