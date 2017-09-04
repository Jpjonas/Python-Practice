def fichasJuego(m,n):
    """
    Representación de los datos:
    Representamos fichas de un juego con números enteros

    Signatura:
    contaNumeros: int -> int -> void
    El primer parámetro representa el mayor número para el primer número de la ficha
    y el segundo el mayor número para el segundo número de la ficha

    Declaracion de propósito:
    La función imprime todas las fichas de un juegos como dominó pero com fichas mas o menos fichas.

    Ejemplos:
    >>> fichasJuego(2,5)={00,01,02,03,04...23,24,25}
    >>> fichasJuego(10,12)={00,01,02,03,04...1011,1012}
    >>> fichasJuego(8,2)={00,01,02,03,04...81,82}
    """
    for x in range (1,m):
        for y in range(1,n):
            print(x,y)

fichasJuego(8,9)
