def fichasDominó():
    """
    Representación de los datos:
    Representamos las fichas de un dominó con números

    Signatura:
    contaNumeros: void -> void

    Declaracion de propósito:
    La función imprime en la pantalla todas las fichas de un dominó sin repetir.

    Ejemplos:
    >>> fichasDominó()={00,01,02,03,04...64,65,66}
    """
    for x in range (1,7):
        for y in range(1,7):
            print(x,y)

fichasDomino()
