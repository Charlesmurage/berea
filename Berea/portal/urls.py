from django.conf.urls import url
from . import views
from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns =[
    url(r'^$', views.signup, name='home'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name= 'portal/login.html'), name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^new/class$', views.new_class, name='new-class'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'^$', views.home, name='home'),
    url(r'^tutorsignup/$', views.signup_view, name='tutorsignup'),
    url(r'^new/class$', views.new_class, name='new-class'),

]