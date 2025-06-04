from django.urls import path

from . import views

urlpatterns = [
    path('', views.books, name ='books_list'),
    path('special/', views.featuredBooks, name ='featured_books_list'),
]