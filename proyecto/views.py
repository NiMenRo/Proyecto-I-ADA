
from django.shortcuts import render, redirect
from django.http import HttpResponse

from algoritmos.smart_terminal_ingenua import transformar_fuerza_bruta
import time
# Create your views here.

# Pagina de inicio
def index(request):
    return render(request, 'index.html')


def terminal_home(request):
    return render(request, 'terminal_home.html')

def subasta_home(request):
    return render(request, 'subasta_home.html')


def terminal_ingenua(request):
    if request.method == 'GET':
        return render(request, 'terminal_ingenua.html')
    else:
        # aca ejecuto una función que puede demorar un poco y retorno una respuesta que deseo que se muestre en la pagina html
        profundidad = request.POST.get('profundidad', '10')  # Asigna '10' por defecto como cadena

        if profundidad.isdigit():  # Verifica si la cadena es un número válido
            profundidad = int(profundidad)
        else:
            profundidad = 10  # Si no es un número válido, asigna 10 como valor por defecto
                
        print(profundidad)
        tiempo_inicial = time.time()
        resultado = transformar_fuerza_bruta(request.POST['cadena_inicial'], request.POST['cadena_objetivo'], profundidad)
        tiempo_final = time.time()
        print("profundiadad: ", profundidad)
        return render(request, 'terminal_ingenua_respuesta.html', {'resultado': resultado, 'tiempo_ejecucion': tiempo_final - tiempo_inicial})
    
def terminal_ingenua_respuesta(request):
    return render(request, 'terminal_ingenua_respuesta.html')