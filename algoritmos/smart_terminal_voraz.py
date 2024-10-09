"""
Autor: Nicolas Mauricio Rojas
Codigo: 2259460
Fecha 4/10/2024
"""
 
import time

def advance(posicion): 
    return posicion + 1


def delete(cadena,posicion):
    if posicion >= len(cadena):
         nueva_posicion = len(cadena) - 1
    else:
        cadena.pop(posicion)
        nueva_posicion = advance(posicion - 1)#Al eliminar un caracter el tamaño de la cadena se reduce

    # Si la posición es inválida, devolver la cadena y la misma posición
    return cadena, nueva_posicion

def replace(cadena, posicion, caracter):
    if posicion < len(cadena):
        cadena[posicion] = caracter
        nueva_posicion = advance(posicion)
        return cadena, nueva_posicion
    return cadena, posicion

def insert(cadena,posicion,caracter):
    #Es el caso cuando la posicon que ingresa es 0
    if posicion == 0:
        cadena.insert(0,caracter)

    elif posicion <= len(cadena) and posicion != 0:
        cadena.insert(posicion, caracter)

    return cadena, posicion + 1

def kill(cadena, posicion):
    if posicion < len(cadena):
        del cadena[posicion:]
    return cadena, posicion

#Una funcion que retorna la cantidad de caracteres que coinciden con la cadenaObjetivo
def guia(cadena, cadenaObjetivo):
    contador = 0
    longitud_minima = min(len(cadena), len(cadenaObjetivo))
    
    for i in range(longitud_minima):
        if cadena[i] == cadenaObjetivo[i]:
            contador += 1
    
    return contador

#Funcion que calcula todas las opciones que puede generar una cadena
def evaluar_opciones(opciones, cadenaObjetivo):
    evaluaciones = []

    for opcion in opciones:
        cadena, pos, operacion = opcion
        coincidencias = guia(cadena, cadenaObjetivo)
        evaluaciones.append((cadena, pos, operacion, coincidencias))

    return evaluaciones

#Funcion que elije la mejor opcion de entre todas las opciones
def mejor_opcion(evaluaciones):
    mejor = None
    max_coincidencias = -1
    max_longitud = -1  # Para manejar caracteres excedentes

    for evaluacion in evaluaciones:
        cadena, pos, operacion, coincidencias = evaluacion
       
        # Priorizar más coincidencias
        if coincidencias > max_coincidencias:
            mejor = evaluacion
            max_coincidencias = coincidencias
            max_longitud = len(cadena)
        elif coincidencias == max_coincidencias:
            # Si las coincidencias son iguales, preferir menor longitud (eliminar excedentes)
            if len(cadena) < max_longitud:
                mejor = evaluacion
                max_longitud = len(cadena)

    return mejor

# Función voraz para transformar la cadena
def transformar_cadena_voraz(cadenaOriginal, cadenaObjetivo):
    # Convertir las cadenas a listas para manipulación
    if isinstance(cadenaOriginal, str):
        cadenaOriginal = list(cadenaOriginal)
    if isinstance(cadenaObjetivo, str):
        cadenaObjetivo = list(cadenaObjetivo)

    posicion = 0
    operaciones_realizadas = 0
    movimientos = {"advance": 0, "replace": 0, "insert": 0, "delete": 0, "kill": 0}  # Variable para almacenar movimientos
    # Inicializar una lista para almacenar la secuencia de movimientos
    movimientos_secuencia = []

    while True:
        # Caso base: cadenaOriginal == cadenaObjetivo
        if cadenaOriginal == cadenaObjetivo:

             # Formatear el resultado de los movimientos al estilo "5a + 1r"
            movimientos_str = " + ".join([f"{v}{k[0]}" for k, v in movimientos.items() if v > 0])
            
            movimientoslist = ",".join(movimientos_secuencia)

            return ''.join(cadenaObjetivo),movimientos_str,movimientoslist
        
        # Arreglo vacío que almacenará las opciones
        opciones = []

        # Opción de avanzar si el carácter actual coincide
        if posicion < len(cadenaOriginal) and posicion < len(cadenaObjetivo) and cadenaOriginal[posicion] == cadenaObjetivo[posicion]:
            nueva_posicion = advance(posicion)
            opciones.append((cadenaOriginal[:], nueva_posicion, "advance"))

        # Opción de reemplazar si el carácter actual no coincide
        if posicion < len(cadenaOriginal) and posicion < len(cadenaObjetivo) and cadenaOriginal[posicion] != cadenaObjetivo[posicion]:
            char_objetivo = cadenaObjetivo[posicion]
            nueva_cadena, nueva_posicion_rep = replace(cadenaOriginal[:], posicion, char_objetivo)
            opciones.append((nueva_cadena, nueva_posicion_rep,"replace"))

        # Opción de insertar si falta un carácter en la posición actual
        if posicion < len(cadenaObjetivo):
            char_a_insertar = cadenaObjetivo[posicion]
            nueva_cadena, nueva_posicion_ins = insert(cadenaOriginal[:], posicion, char_a_insertar)
            opciones.append((nueva_cadena, nueva_posicion_ins,"insert"))

        # Opción de eliminar si hay un carácter extra en la posición actual
        if posicion < len(cadenaOriginal) and (posicion >= len(cadenaObjetivo) or cadenaOriginal[posicion] != cadenaObjetivo[posicion]):
            nueva_cadena, nueva_posicion_del = delete(cadenaOriginal[:], posicion)
            opciones.append((nueva_cadena, nueva_posicion_del, "delete"))

        # Opción de matar si la cadenaOriginal tiene más caracteres que cadenaObjetivo
        if len(cadenaOriginal) > len(cadenaObjetivo) and posicion >= len(cadenaObjetivo):
            nueva_cadena, nueva_posicion_kill = kill(cadenaOriginal[:], posicion)
            opciones.append((nueva_cadena, nueva_posicion_kill, "kill"))

        # Evaluar todas las opciones
        evaluaciones = evaluar_opciones(opciones, cadenaObjetivo)
        
        if not evaluaciones:
            # No hay más operaciones posibles; la transformación falla
            return None

        # Seleccionar la mejor opción
        mejor = mejor_opcion(evaluaciones)
        
        if mejor is None:
            # No se pudo encontrar una mejor opción; la transformación falla
            return None

        # Actualizar la cadena y la posición
        cadenaOriginal, posicion, operacion, coincidencias = mejor
        movimientos[operacion] += 1  # Registrar operación realizada
        operaciones_realizadas += 1
        movimientos_secuencia.append(operacion)  # Registrar operación realizada

        print(f"Operacion {operaciones_realizadas}: {operacion}")
        print(f"Resultado: {''.join(cadenaOriginal)}")
        print(f"Posicion: {posicion}\n")
        #print(evaluaciones)

#------------------------------------Funciones para medir el timepo--------------------------------------------------------------------------#

def medir_tiempo(cadenaOriginal, cadenaObjetivo, num_ejecuciones=50):
    tiempos = []
    for _ in range(num_ejecuciones):
        inicio = time.time()
        transformar_cadena_voraz(cadenaOriginal, cadenaObjetivo)
        fin = time.time()
        tiempos.append(fin - inicio)
    
    # Calcular el tiempo promedio de ejecución sin usar librerías externas
    tiempo_promedio = sum(tiempos) / len(tiempos)
    return tiempo_promedio

def ejecutar_experimentos():
    # Definir los 5 casos de crecimiento (ejemplos)
    casos = [
        ("hola", "pato"),
        ("electricidad", "electrolitros"),
        ("planificacionestrategica", "implementacionpractica"),
        ("transformacionpoderosa", "deformacioncontrolable"),
        ("Electroencefalografista", "Otorrinolaringologicalisimamente")
    ]
    
    # Almacenar los resultados
    resultados = []

    # Ejecutar el algoritmo 50 veces para cada caso y medir el tiempo promedio
    for cadenaOriginal, cadenaObjetivo in casos:
        tiempo_promedio = medir_tiempo(cadenaOriginal, cadenaObjetivo, num_ejecuciones=50)
        resultados.append((cadenaOriginal, cadenaObjetivo, tiempo_promedio))
        print(f"Tiempo promedio para transformar '{cadenaOriginal}' a '{cadenaObjetivo}': {tiempo_promedio:.6f} segundos")
    
    return resultados


def calcular_costo_voraz(secuencia_operaciones, costo_advance, costo_delete, costo_replace, costo_insert, costo_kill):
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





#------------------------------------------------FIN----------------------------------------------------------------------------#


if __name__ == "__main__":
    
    #Cadenas de prueba
    #cadenaOriginal = "Electroencefalografista"
    #cadenaObjetivo = "Otorrinolaringologicalisimamente"

    #cadenaOriginal = "eraseunavezunsimiotrepadoencimadeunarbolcomiendoseunabanana"
    #cadenaObjetivo = "habiaunavezunconejoqueeramuchisimomasvelozqueunatortugaperoperdio"

    #cadenaOriginal = "transformacionpoderosa"
    #cadenaObjetivo = "deformacioncontrolable"

    cadenaOriginal = "hola"
    cadenaObjetivo = "pato"

    # Iniciar cronómetro
    start_time = time.time()

    resultado, movimientos, movimientoslist = transformar_cadena_voraz(cadenaOriginal, cadenaObjetivo)

    # Detener cronómetro
    end_time = time.time()

    # Calcular el tiempo transcurrido
    execution_time = end_time - start_time


    if resultado:
        print(f"Transformacion exitosa: {resultado}")
        print(f"Movimientos realizados: {movimientos}")
        print(f"Secuencia de movimientos: {movimientoslist}")
        print(f"Tiempo de ejecucion: {execution_time:.15f} segundos")
        print(calcular_costo_voraz(movimientoslist.split(','), 1, 1, 1, 1, 1))
    else:
        print("No se pudo transformar la cadena utilizando las opciones disponibles.")


    #--------------------------------Tiempo promedio de ejecutar 50 veces-------------------------------------------------------------#
    # # Ejecutar el experimento
    # resultados = ejecutar_experimentos()

    # # Mostrar los resultados
    # for resultado in resultados:
    #     print(f"De '{resultado[0]}' a '{resultado[1]}': {resultado[2]:.15f} segundos")