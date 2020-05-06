
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from portal import views
from portal.views import signup, home, classes, notes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^portal/', include('portal.urls')),
    path('signup/', signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='portal/login.html'), name="login"),
    path('tutorlogin/',auth_views.LoginView.as_view(template_name='tutorlogin.html'),name='tutorlogin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='portal/logout.html'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view, {'next_page': 'tutorlogin'}, name='tutorlogout'),
    path('classes/',views.classes, name="classes"),
    url(r'classes/units/all/(\d+)/', views.units, name="unit"),
    url(r'classes/units/notes/all/(\d+)/',views.notes, name="notes"),
    
    path('StudentPortal/',home, name='studentportal')
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)