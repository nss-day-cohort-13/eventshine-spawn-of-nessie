from django.conf.urls import url
from . import views
app_name = 'nessie'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/', views.Register.as_view(), name='register'),

    url(r'^login_user/', views.login_user, name='login_user'),

    url(r'^login/', views.Login.as_view(), name='login'),

    url(r'^login/', views.logout_user, name='logout'),

    url(r'^register_user/', views.register_user, name='register_user'),

    url(r'event/add$', views.EventCreate.as_view(), name='event_add'),

    url(r'event_user/add$', views.EventUserCreate.as_view(), name='event_user'),
]
