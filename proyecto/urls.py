from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('terminal/', views.terminal_home, name='terminal_home'),
    path('subasta/', views.subasta_home, name='subasta_home'),
]