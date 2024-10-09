from django.urls import path
from . import views

urlpatterns = [
    
    # paginas principales
    path('', views.index, name='index'),
    path('terminal/', views.terminal_home, name='terminal_home'),
    path('subasta/', views.subasta_home, name='subasta_home'),
    
    # sub-menus
    path('terminal/ingenua/', views.terminal_ingenua, name='terminal_ingenua'),
    # path('terminal/dinamica/', views.terminal_dinamica, name='terminal_dinamica'),
    path('terminal/voraz/', views.terminal_voraz, name='terminal_voraz'),
    # path('subasta/ingenua/', views.subasta_ingenua, name='subasta_ingenua'),
    # path('subasta/dinamica/', views.subasta_dinamica, name='subasta_dinamica'),
    # path('subasta/voraz/', views.subasta_voraz, name='subasta_voraz'),
]