from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import  re_path
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^send-email/$', views.send_email, name='send_email'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
