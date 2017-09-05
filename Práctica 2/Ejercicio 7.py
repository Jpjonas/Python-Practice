def numTriangulares(n):
    """
    Representación de los datos:
    Representamos números triangulares con enteros

    Signatura:
    contaNumeros: int -> void
    El parámetro es la cantidad de números triangulares

    Declaracion de propósito:
    La función imprime la cantidad de números triangulares deseados.

    Ejemplos:
    >>> contaNumeros(2,5)={2,3,4,5}
    >>> contaNumeros(10,12)={10,11,12}
    >>> contaNumeros(-10,-5)={-10,-9,-8,-7,-6,-5}
    """
    t=0
    for x in range(1,n+1):
        t=t+x
        print(x," - ",t)


def numTriangulares2(n):
    for x in range (1,n+1):
        print(x," - ",int(x*(x+1)/2))

numTriangulares(10)
numTriangulares2(10)
