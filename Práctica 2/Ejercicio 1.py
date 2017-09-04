def contaNumeros(n,m):
    """
    Representación de los datos:
    Representamos números como enteros

    Signatura:
    contaNumeros: int -> int -> void
    El primer parámetro representa el número inicial de la contagen,
    y el segundo el número final.

    Declaracion de propósito:
    La función imprime todos los números naturales en un intervalo.

    Ejemplos:
    >>> contaNumeros(2,5)={2,3,4,5}
    >>> contaNumeros(10,12)={10,11,12}
    >>> contaNumeros(-10,-5)={-10,-9,-8,-7,-6,-5}
    """
    for x in range(n,m+1):
        print(x)


contaNumeros(1,50)
