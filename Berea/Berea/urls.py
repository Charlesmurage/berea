
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from portal import views
from portal.views import  classes


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^portal/', include('portal.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='portal/logout.html'), name='logout'),
    path('classes/all',views.classes, name="classes"),
    path('student/',include('Student.urls'), name='studentportal')
    

]
