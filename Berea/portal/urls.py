from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.home_view, name='home'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name= 'portal/login.html'), name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

]