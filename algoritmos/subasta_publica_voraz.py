"""
Autor: Victor Hernandez
Codigo: 2259520
Titulo: Algoritmo Voraz De La Subasta
"""
def subasta_publica_voraz(A: int, B: int, n: int, ofertas: list) -> dict:
    
    # asigno numero de oferente a las ofertas
    ofertas_numero_oferente = []
    for i in range(n):
        ofertas_numero_oferente.append((i, ofertas[i]))
    
    # ordernar por las ofertas mas altas, ofertas con numero de oferente, selecciono el precio
    ofertas_ordenadas = sorted(ofertas_numero_oferente, key=lambda oferta: oferta[1][0], reverse=True)
    
    # inicializo variables
    acciones_compradas_lista = []  # lista con el número de acciones asignadas por oferente
    vr = 0 
    
    for oferta in ofertas_ordenadas:
        if A == 0:
            break
        if oferta[1][0] >= B:  # valido el precio minimo
            acciones_compradas = min(oferta[1][2], A)  # asigno las acciones que puedo comprar
            if acciones_compradas >= oferta[1][1]:  # verifico si cumple el minimo de requerido
                A -= acciones_compradas
                acciones_compradas_lista.append((oferta[0], acciones_compradas))
                vr += acciones_compradas * oferta[1][0]
    
    # acciones sobrantes las compra el gobierno
    if A > 0:
        vr += A * B
        acciones_compradas_lista.append(("Gobierno", A))
    
    # retorno un diccionario
    return {
        "vr": vr,
        "acciones_compradas": acciones_compradas_lista
    }


if __name__ == "__main__":
    A = 1922
    B = 100
    ofertas = [
        (850, 50, 150),
        (700, 100, 300),
        (900, 20, 200),
        (600, 50, 250),
        (750, 80, 180),
        (500, 30, 130),
        (650, 60, 300),
        (400, 20, 220),
        (300, 10, 100),
        (950, 100, 400),
        (1000, 200, 500),
        (550, 30, 150),
        (450, 50, 170),
        (800, 120, 320),
        (700, 100, 250),
        (900, 80, 200),
        (350, 20, 90),
        (600, 60, 160),
        (750, 50, 200),   
        (400, 20, 80)     
    ]

    n = len(ofertas)

    resultado = subasta_publica_voraz(A, B, n, ofertas)
    print("Valor total recibido:", resultado["vr"])
    print("Acciones compradas:", resultado["acciones_compradas"])   