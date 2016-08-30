from django.conf.urls import url
from . import views
app_name = 'nessie'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/', views.Register.as_view(), name='register'),

    url(r'^loginUser/', views.loginUser.as_view(), name='loginUser'),

    url(r'^logout/', views.logoutUser.as_view(), name='logout'),

    url(r'^failedLogin/', views.failedLogin.as_view(), name='failedLogin'),

    url(r'^register_user/', views.register_user, name='register_user'),

    url(r'event/add$', views.EventCreate.as_view(), name='event_add'),
]
