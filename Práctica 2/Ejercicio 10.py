def mayor():
    """
    Representación de los datos:
    Representamos números como números

    Signatura:
    contaNumeros: void -> void

    Declaracion de propósito:
    La función pide dos números y verifica si el segundo es mayor que el primer.

    Ejemplos:
    >>> mayor() 4 5=4 5
    >>> mayor() 4 3 4 5=4 5
    >>> mayor() 10 8 7 12=10 12
    """
    a=int(input("Informe el primer número: "))
    b=0
    while(b<a):
        b=int(input("Informe el segundo número: "))
    print(a," - ",b)

mayor()
