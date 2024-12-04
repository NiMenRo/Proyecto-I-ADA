import time

def calcular_matriz_costos(cadena1, cadena2, costos):
    n = len(cadena1)
    m = len(cadena2)
    
    # Extraemos los costos de las operaciones
    a = costos['advance']
    d = costos['delete']
    r = costos['replace']
    i = costos['insert']
    k = costos['kill']
    
    # Crear matriz de tamaño (n+1) x (m+1)
    M = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Inicialización de casos base
    for x in range(1, n + 1):
        M[x][0] = x * d  # Eliminar todos los caracteres de cadena1
    for y in range(1, m + 1):
        M[0][y] = y * i  # Insertar todos los caracteres en cadena2
    
    # Llenado de la matriz
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            opciones = []
            
            # Opción: advance (si los caracteres coinciden)
            if cadena1[x - 1] == cadena2[y - 1]:
                opciones.append(M[x - 1][y - 1] + a)
            
            # Opción: delete
            opciones.append(M[x - 1][y] + d)
            
            # Opción: replace
            opciones.append(M[x - 1][y - 1] + r)
            
            # Opción: insert
            opciones.append(M[x][y - 1] + i)
            
            # Guardar el mínimo costo
            M[x][y] = min(opciones)
    
    # Considerar la operación 'kill' para la última fila
    for x in range(1, n + 1):
        M[x][m] = min(M[x][m], M[x - 1][m] + k)
    
    return M

def reconstruir_operaciones(cadena1, cadena2, M, costos):
    n = len(cadena1)
    m = len(cadena2)
    
    a = costos['advance']
    d = costos['delete']
    r = costos['replace']
    i = costos['insert']
    k = costos['kill']
    
    operaciones = []
    movimientos = {"advance": 0, "replace": 0, "insert": 0, "delete": 0, "kill": 0}
    x, y = n, m  # Empezamos desde la esquina inferior derecha de la matriz
    cursor = n
    while x > 0 or y > 0:
        if x > 0 and y > 0 and cadena1[x - 1] == cadena2[y - 1]:
            if M[x][y] == M[x - 1][y - 1] + a:
                operaciones.append(f"advance (mantener '{cadena1[x-1]}')")
                movimientos['advance'] += 1
                x -= 1
                y -= 1
                continue

        if x > 0 and y > 0 and M[x][y] == M[x - 1][y - 1] + r:
            operaciones.append(f"replace '{cadena1[x-1]}' con '{cadena2[y-1]}'")
            movimientos['replace'] += 1
            x -= 1
            y -= 1
        elif x > 0 and M[x][y] == M[x - 1][y] + d:
            operaciones.append(f"delete '{cadena1[x-1]}'")
            movimientos['delete'] += 1
            x -= 1
        elif y > 0 and M[x][y] == M[x][y - 1] + i:
            operaciones.append(f"insert '{cadena2[y-1]}'")
            movimientos['insert'] += 1
            y -= 1
        else:
            x > 0 and M[x][y] == M[x - 1][m] + k
            operaciones.append(f"kill desde posición {cursor}")
            movimientos['kill'] += 1
            x = 0
        cursor = m
        

    operaciones.reverse()  # Invertimos para obtenerlas en orden
    return operaciones, movimientos

def calcularmovimientos(movimientos):
    costo_terminos = (f"{movimientos['advance']}a + {movimientos['delete']}d + {movimientos['replace']}r + {movimientos['insert']}i  + {movimientos['kill']}k")
    return costo_terminos

def generar_costo(movimientos, costos):
    sumd = movimientos['delete'] * costos['delete']
    sumi = movimientos['insert'] * costos['insert']
    sumr = movimientos['replace'] * costos['replace']
    suma = movimientos['advance'] * costos['advance']
    sumk  = movimientos['kill'] * costos['kill']
    sumatotal = suma+sumd+sumr+sumi+sumk
    return sumatotal

if __name__ == "__main__":
    start_time = time.time()
    cadena1 = "frencesaweq"
    cadena2 = "ancestro"
    
    costos = {
        'advance': 1,
        'delete': 2,
        'replace': 3,
        'insert': 2,
        'kill': 1
    }
    
    
    M = calcular_matriz_costos(cadena1, cadena2, costos)
    operaciones,movimientos = reconstruir_operaciones(cadena1, cadena2, M, costos)
    costoterminos = calcularmovimientos(movimientos)

    costoTotal = generar_costo(movimientos, costos)

    
    print("Operaciones óptimas:")
    for op in operaciones:
        print(op)

    print(f"\nCosto: {costoTotal}")  
    print(f"Costo en términos de operaciones: {costoterminos}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time:f} segundos\n")