
from django.shortcuts import render


from algoritmos.smart_terminal_ingenua import transformar_fuerza_bruta, calcular_costo
from algoritmos.smart_terminal_voraz import transformar_cadena_voraz, calcular_costo_voraz
from algoritmos.smart_terminal_dinamico import calcular_matriz_costos, reconstruir_operaciones, generar_costo ,calcularmovimientos
import time
# Create your views here.

# Pagina de inicio
def index(request):
    return render(request, 'index.html')


def terminal_home(request):
    return render(request, 'terminal/terminal_home.html')

def subasta_home(request):
    return render(request, 'subasta_home.html')

def terminal_datos(request, solucion, titulo_solucion):
    return render(request, 'terminal/terminal_datos.html', {'solucion': solucion, 'titulo_solucion': titulo_solucion})

def terminal_ingenua(request):
    if request.method == 'GET':
        return terminal_datos(request, 'ingenua', 'Solución Ingenua/Fuerza Bruta')
    else:
        # aca ejecuto una función que puede demorar un poco y retorno una respuesta que deseo que se muestre en la pagina html
        profundidad = request.POST.get('profundidad', '10')  # Asigna '10' por defecto como cadena

        if profundidad.isdigit():  # Verifica si la cadena es un número válido
            profundidad = int(profundidad)
        else:
            profundidad = 10  # Si no es un número válido, asigna 10 como valor por defecto

        tiempo_inicial = time.time()
        resultado = transformar_fuerza_bruta(request.POST['cadena_inicial'], request.POST['cadena_objetivo'], profundidad)
        costos = calcular_costo(resultado, int(request.POST['advance']), int(request.POST['delete']), 
                                int(request.POST['replace']), int(request.POST['insert']), 
                                int(request.POST['kill']))
        tiempo_final = time.time()
        print("profundiadad: ", profundidad)
        return render(request, 'terminal/terminal_ingenua_respuesta.html',
                      {'cadena_inicial': request.POST['cadena_inicial'], 'cadena_objetivo': request.POST['cadena_objetivo'],'resultado': resultado, 'tiempo_ejecucion': tiempo_final - tiempo_inicial,
                       'ecuacion_costos_variables': costos[0], 'ecuacion_costos': costos[1], 'costo_total': costos[2]})
    
def terminal_voraz(request):
    if request.method == 'GET':
        return terminal_datos(request, 'voraz', 'Solución Voraz')
    else:
        tiempo_inicial = time.time()
        resultado = transformar_cadena_voraz(request.POST['cadena_inicial'], request.POST['cadena_objetivo'])
        costos = calcular_costo_voraz(resultado[2].split(','), int(request.POST['advance']), int(request.POST['delete']), 
                        int(request.POST['replace']), int(request.POST['insert']), 
                        int(request.POST['kill']))
        tiempo_final = time.time()
        return render(request, 'terminal/terminal_voraz_respuesta.html',
                      {'cadena_inicial': request.POST['cadena_inicial'], 'cadena_objetivo': request.POST['cadena_objetivo'],'resultado': f"({resultado[2]})", 'tiempo_ejecucion': tiempo_final - tiempo_inicial,
                       'ecuacion_costos_variables': costos[0], 'ecuacion_costos': costos[1], 'costo_total': costos[2]})

def terminal_dinamica(request):
    if request.method == 'GET':
        return terminal_datos(request, 'dinamica', 'Solución Dinámica')
    else:
        # recogemos la cadena inicial (x) y la cadena objetivo (y)
        X = request.POST['cadena_inicial']
        Y = request.POST['cadena_objetivo']
        
        print(len(X))
        print(len(Y))
        # recogemos los costos de cada operacion
        costos = {
        'advance': int(request.POST['advance']),
        'delete': int(request.POST['delete']),
        'replace': int(request.POST['replace']),
        'insert': int(request.POST['insert']),
        'kill': int(request.POST['kill'])
        }
        
        tiempo_inicial = time.time()
        # Calcular el costo mínimo y la matriz de soluciones
        M = calcular_matriz_costos(X, Y, costos)
        operaciones_optimas, movimientos = reconstruir_operaciones(X, Y, M, costos)
        costoterminos = calcularmovimientos(movimientos)
        costoTotal = generar_costo(movimientos, costos)
        
        tiempo_final = time.time()
        tiempo_total = str(tiempo_final - tiempo_inicial)
        print(tiempo_total)
        
        
        return render(request, 'terminal/terminal_dinamica_respuesta.html',
                    {'cadena_inicial': request.POST['cadena_inicial'], 
                    'cadena_objetivo': request.POST['cadena_objetivo'],'resultado': operaciones_optimas, 'tiempo_ejecucion': tiempo_total,
                    'costo_operaciones': costoterminos, 'costo_minimo': costoTotal})