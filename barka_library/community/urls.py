from django.urls import path

from . import views

urlpatterns = [
    path('', views.events, name ='community_events'),
]