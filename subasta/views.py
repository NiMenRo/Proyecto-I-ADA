from django.shortcuts import render

# Create your views here.

def subasta_home(request):
    return render(request, 'subasta/subasta_home.html')