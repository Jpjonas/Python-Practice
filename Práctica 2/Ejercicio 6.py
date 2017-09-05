def inversiones(c,x,n):
    """
    Representación de los datos:
    Representamos inversiones con números

    Signatura:
    contaNumeros: float -> float ->  int -> void
    El primer parámetro representa el capital inicial, el segundo la tasa de interés,
    y el tercer el número de años a calcular.
    Declaracion de propósito:
    La función calcula el monto final a otener.

    Ejemplos:
    >>> inversiones(10,90,10) = 6131,06
    >>> inversiones(100,70,5) = 1419,85
    >>> inversiones(1500,50,15) = 656840,83
    """
    t=1
    for y in range(0,n):
        t=t*(1+(x/100))
    print(c*t)

#Testes
inversiones(10,90,10)
inversiones(100,70,5)
inversiones(1500,50,15)
