
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Pagina de inicio
def index(request):
    return render(request, 'index.html', {'title': 'Hello','username': 'David', 'password': '1234'})
