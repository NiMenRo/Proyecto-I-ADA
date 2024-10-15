import time

def calcular_costo_minimo(X, Y, costos):
    m, n = len(X), len(Y)
    matriz = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        matriz[i][0] = i * costos['delete']
    for j in range(1, n + 1):
        matriz[0][j] = j * costos['insert']

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1] + costos['advance']
            else:
                matriz[i][j] = min(
                    matriz[i - 1][j] + costos['delete'],
                    matriz[i][j - 1] + costos['insert'],
                    matriz[i - 1][j - 1] + costos['replace']
                )
    for i in range(1, m + 1):
        matriz[i][n] = min(matriz[i][n], matriz[i - 1][n] + costos['kill'])
    
    return matriz[m][n], matriz
    # **Agregar la operación `kill`**
    # En la última fila, evaluamos si es mejor realizar `kill` y borrar todos los caracteres restantes
    '''for i in range(1, n + 1):
        M[i][m] = min(M[i][m], M[i - 1][m] + costos['kill'])

    return M[n][m], M
'''
# Función para construir la secuencia de operaciones óptimas a partir de la matriz de costos
def construir_solucion_optima(M, X, Y, costos):
    i, j = len(X), len(Y)
    operaciones = []
    movimientos = {"advance": 0, "replace": 0, "insert": 0, "delete": 0, "kill": 0}
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and X[i - 1] == Y[j - 1]:
            operaciones.append(f"Avanzar: {X[i - 1]}")
            movimientos['advance'] += 1
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and M[i][j] == M[i - 1][j - 1] + costos['replace']:
            operaciones.append(f"Reemplazar {X[i - 1]} con {Y[j - 1]}")
            movimientos['replace'] += 1
            i -= 1
            j -= 1
        elif i > 0 and M[i][j] == M[i - 1][j] + costos['delete']:
            operaciones.append(f"Borrar: {X[i - 1]}")
            movimientos['delete'] += 1
            i -= 1
        elif j > 0 and M[i][j] == M[i][j - 1] + costos['insert']:
            operaciones.append(f"Insertar: {Y[j - 1]}")
            movimientos['insert'] += 1
            j -= 1
        elif i > 0 and M[i][j] == M[i - 1][j] + costos['kill']:
            operaciones.append(f"Kill desde posición {i}")
            movimientos['kill'] += 1
            i = 0  # Terminar la secuencia de operaciones, ya que `kill` elimina el resto
    
    operaciones.reverse()  # Invertimos para mostrar el orden correcto
    return operaciones,movimientos

def generar_costo(movimientos):
    costo_str = " + ".join([f"{v}{k[0]}" for k, v in movimientos.items() if v > 0])
    return costo_str

# Función principal
if __name__ == "__main__":
    star_time = time.time()
    X = "frencesaweq"
    Y = "ancestro"
    
    # Definir los costos de las operaciones
    costos = {
        'advance': 1,
        'delete': 2,
        'replace': 3,
        'insert': 2,
        'kill': 1
    }
    
    # Calcular el costo mínimo y la matriz de soluciones
    costo_minimo, matriz = calcular_costo_minimo(X, Y, costos)
    
    # Construir la secuencia de operaciones óptima
    operaciones_optimas, movimientos = construir_solucion_optima(matriz, X, Y, costos)

    costo_operaciones = generar_costo (movimientos)
    
    # Imprimir los resultados
    
    print("Operaciones óptimas:")
    for op in operaciones_optimas:
        print(op)
        
    print(operaciones_optimas)

    print(f"\nCosto mínimo: {costo_minimo}")  
    print(f"Costo en términos de operaciones: {costo_operaciones}")
    End_time = time.time()
    execution_time = End_time - star_time
    print(f"Tiempo de ejecución: {execution_time} segundos\n")