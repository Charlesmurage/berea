from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns =[
    url(r'^$', views.signup, name='home'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^new/class$', views.new_class, name='new-class'),

]