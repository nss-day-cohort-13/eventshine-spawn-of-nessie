from django.conf.urls import url
from . import views
app_name = 'nessie'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', views.UserLoginView.as_view(), name='login'),

    url(r'event/add$', views.EventCreate.as_view(), name='event_add'),
]
