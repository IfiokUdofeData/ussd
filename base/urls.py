from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ussd', views.ussd_callback, name='ussd_callback'),
]
