from django.urls import path, include
from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.main, name='main'),  #eth viwe function um ayt ann connect cheyunnath... enn kanikan
    path('about/', views.about, name='about'),
    # path('login/', views.login, name='login'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('gallary/', views.gallary, name='gallary'),
    path('api/create_event/', views.createEvent, name='createEvent'),
    # path('api/delete_event/', views.deleteEvent, name='deleteEvent'),
]
