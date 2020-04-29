from django.conf.urls import url
from . import views
from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns =[
    url(r'^$', views.home, name='home'),
    url(r'^tutorsignup/$', views.signup_view, name='tutorsignup'),
    url(r'^new/class$', views.new_class, name='new-class'),

]