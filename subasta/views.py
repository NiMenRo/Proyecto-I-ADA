from django.http import HttpResponse
from django.shortcuts import render
from algoritmos.subasta_publica_voraz import subasta_publica_voraz
from algoritmos.subasta_publica_dinamico import subasta_publica_dinamico
import time

# Create your views here.

def subasta_home(request):
    return render(request, 'subasta/subasta_home.html')

def subasta_datos(request, solucion, rango, titulo_solucion):
    return render(request, 'subasta/subasta_datos.html', {'solucion': solucion, 'rango': rango, 'n': len(rango), 'titulo_solucion': titulo_solucion})


def subasta_voraz(request):
    if request.method == 'GET':
        return subasta_datos(request, request.GET['algoritmo'], range(int(request.GET['n'])), 'Solución Voraz')
    else:
        # Organizar las ofertas
        ofertas = []
        for i in range(int(request.POST['n'])): # precio, minimo_acciones, maximo_acciones
            ofertas.append((int(request.POST[f'p{i}']), int(request.POST[f'min{i}']), int(request.POST[f'max{i}'])))
            
        print("ofertas\n", ofertas)
        # extraer acciones y precio minimo
        A = int(request.POST['cantidad_acciones'])
        B = int(request.POST['precio_minimo'])
        
        # ejecuto el algoritmo
        tiempo_inicial = time.time()
        solucion = subasta_publica_voraz(A, B, int(request.POST['n']), ofertas)
        tiempo_final = time.time()
        print("solucion\n", solucion)
        print("tiempo\n", tiempo_final - tiempo_inicial)
        print(f"tiempo: {tiempo_final - tiempo_inicial:.100f}")
        
        # organizar acciones compradas como diccionario
        acciones_compradas = {}
        for ofertante, acciones in solucion['acciones_compradas']:
            acciones_compradas[ofertante] = acciones
            
        # envio los datos correspondientes al template
        return render(request, 'subasta/subasta_voraz_respuesta.html', {'vr': solucion['vr'], 'acciones_compradas': acciones_compradas.items(), 'tiempo_ejecucion': f"{tiempo_final - tiempo_inicial:.10f}"})
    
    
def subasta_dinamica(request):
    if request.method == 'GET':
        return subasta_datos(request, request.GET['algoritmo'], range(int(request.GET['n'])), 'Solución Dinámica')
    else:
        # Organizar las ofertas
        
        ofertas = []
        for i in range(int(request.POST['n'])): # precio, minimo_acciones, maximo_acciones
            ofertas.append({'P': int(request.POST[f'p{i}']), 'm': int(request.POST[f'min{i}']), 'M': int(request.POST[f'max{i}'])})
            
        print("ofertas\n", ofertas)
        # extraer acciones y precio minimo
        A = int(request.POST['cantidad_acciones'])
        B = int(request.POST['precio_minimo'])
        
        # ejecuto el algoritmo
        tiempo_inicial = time.time()
        ingreso, asignaciones = subasta_publica_dinamico(A, B, ofertas)
        tiempo_final = time.time()
        
        print("solucion\n", asignaciones)
        print("tiempo\n", tiempo_final - tiempo_inicial)
        print(f"tiempo: {tiempo_final - tiempo_inicial:.100f}")
        
        # organizar acciones compradas como lista de pares ofertante-acciones
        asignacion_final = []
        for i in range(len(asignaciones)):
            asignacion_final.append((i, asignaciones[i]))
        
        print("asignacion_final\n", asignacion_final)
        # envio los datos correspondientes al template
        return render(request, 'subasta/subasta_dinamica_respuesta.html', {'vr': ingreso, 'acciones_compradas':asignacion_final, 'tiempo_ejecucion': f"{tiempo_final - tiempo_inicial:.10f}"})
        