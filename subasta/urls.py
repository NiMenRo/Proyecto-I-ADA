from django.urls import path
from . import views

urlpatterns = [
    
    # paginas principales
    path('subasta/', views.subasta_home, name='subasta_home'),
    
    
    # sub-menus
    # path('subasta/ingenua/', views.subasta_ingenua, name='subasta_ingenua'),
    # path('subasta/dinamica/', views.subasta_dinamica, name='subasta_dinamica'),
    path('subasta/voraz/', views.subasta_voraz, name='subasta_voraz'),
]