
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Pagina de inicio
def index(request):
    return render(request, 'index.html', {'title': 'Hello','username': 'David', 'password': '1234'})



def terminal_home(request):
    return render(request, 'terminal_home.html', {'title': 'Terminal Inteligente','username': 'David', 'password': '1234'})

def subasta_home(request):
    return render(request, 'subasta_home.html', {'title': 'Subasta Inteligente','username': 'David', 'password': '1234'})