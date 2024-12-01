"""
Autor: Nicolas Mauricio Rojas
Codigo: 2259460
Titulo: Algoritmo Dinamico De La Subasta
"""
from timeit import timeit

#A -> Numero de acciones(columnas)
#B -> Valor minimo al que se venderan las acciones
def subasta_publica_dinamico(A,B,oferentes):

    #Añadir al gobierno como un oferente y su oferta maxima sera el minimo dispuesto por el ofertor
    gobierno = {'P': B, 'm': 0, 'M': A}
    oferentes.append(gobierno)

    #Numero de oferentes(filas)
    N = len(oferentes)

    #Crear una tabla de N+1 filas y A+1 Columnas
    subasta = [[-float('inf')] * (A+1) for i in range(N +1)]
    
    #Si no hay oferentes y no hay acciones el resultado es 0
    subasta[0][0] = 0


    for i in range(1, N + 1):
        oferta = oferentes[i-1]
        P = oferta['P'] #Precio a pagar por cada accion
        m = oferta['m'] #Cantidad minima de acciones a comprar
        M = oferta['M'] #Cantidad maxima de acciones a comprar

        for j in range(A+1):
            #No asignar acciones al oferente
            if subasta[i-1][j] > subasta[i][j]:
                subasta[i][j] = subasta[i-1][j]

            
            #Asignar n acciones al oferente i
            # n puede ser desde el minimo hasta el maximo sin exceder A
            for n in range(m,min(M, A - j) + 1):
                if subasta[i-1][j] + P * n > subasta[i][j + n]:
                    subasta[i][j + n] = subasta[i-1][j] + P * n
    
    
    #Ingreso Maximo
    ingreso_maximo = subasta[N][A] #El resultado siempre se encuentra en la ultima fila y columna

    #Recuperar la asignacion
    #Inicializar una lista para almacenar las asignaciones
    asignacion_final = [0] * N

    #i = #oferentes
    #j = #acciones
    i, j = N, A

    while i > 0 and j >= 0:
        if subasta[i][j] == subasta[i-1][j]:
            #No hubo asignaciones al oferente
            i -=1
        else:
            #Se asignaron n acciones al oferente
            asignado = False
            #Como el #oferentes no tiene en cuenta posiciones por eso se resta cuando llamo a oferentes
            for n in range(oferentes[i-1]['m'], min(oferentes[i-1]['M'], j) + 1):
                if j - n >= 0 and subasta[i][j] == subasta[i-1][j - n] + oferentes[i-1]['P'] * n:
                    asignacion_final[i-1] = n
                    j -= n
                    i -= 1
                    asignado = True
                    break
            if not asignado:
                # No se pudo asignar acciones; pasar al siguiente
                i -= 1

    return ingreso_maximo, asignacion_final

if __name__ == '__main__':
        
    A = 20
    B = 100
    oferentes = [
        {'P': 100, 'm': 0, 'M': 5},   # Oferta 1
        {'P': 400, 'm': 10, 'M': 15},   # Oferta 2
        {'P': 500, 'm': 5, 'M': 20},
    ]

    # Configuración de los ejemplos
    ejemplos = [ (20, 100, [{'P': 100, 'm': 0, 'M': 5}, {'P': 400, 'm': 10, 'M': 15}, {'P': 500, 'm': 5, 'M': 20}]),
                (15, 50, [{'P': 200, 'm': 2, 'M': 6}, {'P': 150, 'm': 1, 'M': 3}, {'P': 300, 'm': 4, 'M': 8}]),
                (25, 75, [{'P': 250, 'm': 5, 'M': 10}, {'P': 350, 'm': 7, 'M': 12}, {'P': 450, 'm': 6, 'M': 15}]),
                (18, 90, [{'P': 180, 'm': 3, 'M': 7}, {'P': 380, 'm': 8, 'M': 12}, {'P': 480, 'm': 6, 'M': 10}]),
                (22, 60, [{'P': 220, 'm': 4, 'M': 9}, {'P': 320, 'm': 6, 'M': 11}, {'P': 520, 'm': 7, 'M': 13}]),]


    # Medición del tiempo de ejecución y cálculo del promedio
    for ejemplo in ejemplos: 
        A, B, oferentes = ejemplo 
        tiempo = timeit(lambda: subasta_publica_dinamico(A, B, oferentes.copy()), number=50) 
        promedio = tiempo / 50 
        ingreso, asignacion = subasta_publica_dinamico(A, B, oferentes.copy()) 
        print(f"Ejemplo con A={A}, B={B} promedio de tiempo de ejecucion: {promedio:.5f} segundos") 
        print(f"Ingreso Maximo: {ingreso}") 
        print("Asignacion de acciones a cada oferente:") 
        for idx, acciones in enumerate(asignacion, 1): 
            print(f"Oferente {idx}: {acciones} acciones") 
        print()