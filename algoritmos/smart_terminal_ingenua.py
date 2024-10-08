# solucion ingenua/fuerza bruta para el problema de la terminal inteligente

from itertools import product
import time

# Operaciones
def advance(cadena, cursor):
    if cursor < len(cadena):
        cursor += 1
    return cadena, cursor
def delete(cadena, cursor):
    if 0 <= cursor < len(cadena):  
        cadena = cadena[:cursor] + cadena[cursor+1:]
    cursor = min(cursor, len(cadena) - 1)
    return cadena, cursor
    
def replace(cadena, cursor, caracter):
    if 0 <= cursor < len(cadena):
        cadena = cadena[:cursor] + caracter + cadena[cursor+1:]
        cursor += 1
    return cadena, cursor

def insert(cadena, cursor, caracter):
    if 0 <= cursor <= len(cadena):
        cadena = cadena[:cursor] + caracter + cadena[cursor:]
        cursor += 1
    return cadena, cursor

def kill(cadena, cursor):
    if 0 <= cursor <= len(cadena):
        cadena = cadena[:cursor]
    return cadena, cursor

#### Algoritmo de fuerza bruta ####
def transformar_fuerza_bruta(cadena, cadena_objetivo, max_profundidad=10):
    # lista con las operaciones para generar el producto cartesiano
    operaciones_disponibles = ['advance', 'delete', 'replace', 'insert', 'kill']
    
    # para cada profundidad hasta la profundidad maxima, para cada secuencia de operaciones dentro de todas las combinaciones de 
    # operaciones posibles, ejecuto dicha secuencia de operaciones
    for profundidad in range(1, max_profundidad + 1):
        for secuencia_operaciones in product(operaciones_disponibles, repeat=profundidad): # genero las combinaciones posibles de opreaciones de tamaño profundidad
            # ejecuto la secuencia de operaciones verificando si la solución es la correcta
            resultado = ejecutar_operaciones(cadena, cadena_objetivo, secuencia_operaciones)
            if resultado:
                return secuencia_operaciones # si es correcta, devuelvo la secuencia de operaciones

    return None

def ejecutar_operaciones(cadena, cadena_objetivo, secuencia_operaciones):
    cursor = 0
    for operacion in secuencia_operaciones:
        if operacion == 'advance':
            cadena, cursor = advance(cadena, cursor)
            print(cadena, cursor)
        elif operacion == 'delete':
            cadena, cursor = delete(cadena, cursor)
            print(cadena, cursor)
        elif operacion == 'replace': # a la hora de reemplazar verifico si el cursor esta dentro de las posiciones correctas
                                    # y reemplazo tratando de coincidir con la cadena objetivo
            if cursor < len(cadena_objetivo):
                caracter_a_reemplazar = cadena_objetivo[cursor]
                cadena, cursor = replace(cadena, cursor, caracter_a_reemplazar)
                print(cadena, cursor)
            else:
                return False
        elif operacion == 'insert': # aplico lo mismo que a la hora de reemplazar
            if cursor < len(cadena_objetivo):
                caracter_a_insertar = cadena_objetivo[cursor]
                cadena, cursor = insert(cadena, cursor, caracter_a_insertar)
                print(cadena, cursor)
        elif operacion == 'kill':
            cadena, cursor = kill(cadena, cursor)
            print(cadena, cursor)
    
    return cadena == cadena_objetivo # verifico si las cadenas son iguales y retorno un booleano


def calcular_costo(secuencia_operaciones, costo_advance, costo_delete, costo_replace, costo_insert, costo_kill):
    sum_a = 0
    sum_d = 0 
    sum_r = 0 
    sum_i = 0
    sum_k = 0
    for operacion in secuencia_operaciones:
        if operacion == 'advance':
            sum_a += 1
        elif operacion == 'delete':
            sum_d += 1
        elif operacion == 'replace':
            sum_r += 1
        elif operacion == 'insert':
            sum_i += 1
        elif operacion == 'kill':
            sum_k += 1
            
    a = sum_a * costo_advance
    d = sum_d * costo_delete
    r = sum_r * costo_replace
    i = sum_i * costo_insert
    k = sum_k * costo_kill
    
    ecuacion_costo_variables = f"{sum_a}a + {sum_d}d + {sum_r}r + {sum_i}i + {sum_k}k"
    ecuacion_costo = f"{sum_a}*{costo_advance} + {sum_d}*{costo_delete} + {sum_r}*{costo_replace} + {sum_i}*{costo_insert} + {sum_k}*{costo_kill}"
    
        
    costo_total = a + d + r + i + k
    return ecuacion_costo_variables, ecuacion_costo, costo_total

if __name__ == '__main__':    
    # Prueba con la cadena de ejemplo
    cadena_inicial = "hola"
    cadena_objetivo = "halo"
    tiempo_inicial = time.time()
    resultado = transformar_fuerza_bruta(cadena_inicial, cadena_objetivo, max_profundidad=10)
    tiempo_final = time.time()

    tiempo_ejecucion = tiempo_final - tiempo_inicial

    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

    if resultado:
        print("Secuencia de operaciones encontrada:", resultado)
    else:
        print("No se encontró solución en el límite de profundidad dado.")