from itertools import product
import time

def subasta_fuerza_bruta(A, B, oferentes):
  
    gobierno = {'P': B, 'm': 0, 'M': A}
    oferentes.append(gobierno)
    
    rangos = [range(oferta['m'], oferta['M'] + 1) for oferta in oferentes]
    
    mejor_ingreso = float('-inf')
    mejor_asignacion = None
    combinaciones_evaluadas = 0
    acciones_gobierno = 0

    for combinacion in product(*rangos):
        combinaciones_evaluadas += 1

        if sum(combinacion) == A:
            ingreso = sum(asignacion * oferta['P'] for asignacion, oferta in zip(combinacion, oferentes))
            if ingreso > mejor_ingreso:
                mejor_ingreso = ingreso
                mejor_asignacion = combinacion
                acciones_gobierno = A - sum(combinacion[:-1])
    oferentes.pop()
    return mejor_ingreso, mejor_asignacion[:-1], acciones_gobierno

if __name__ == '__main__':
    
    incio = time.time()
    A = 3000
    B = 50
    oferentes = [
    {'P': 100, 'm': 20, 'M': 300},
    {'P': 500, 'm': 5, 'M': 20}
    ]


    ingreso, asignacion, acciones_gobierno = subasta_fuerza_bruta(A, B, oferentes)

    print(ingreso)
    print(asignacion)
    print(acciones_gobierno)

    print(f"Ingreso máximo: {ingreso}")
    print("Asignación de acciones a cada oferente:")
    for idx, acciones in enumerate(asignacion, 1):
        print(f"Oferente {idx}: {acciones} acciones")
    print (f"Acciones compradas al gobierno: {acciones_gobierno} acciones")

    fin = time.time()
    print(f"Tiempo de ejecución: {fin - incio} segundos")
