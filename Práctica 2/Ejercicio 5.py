def farCel():
    """
    Representación de los datos:
    Representamos temperaturas con números

    Signatura:
    contaNumeros: void -> void

    Declaracion de propósito:
    La función conbierte y imprime todas las temperaturas de 0 hasta 120 F.

    Ejemplos:
    >>> contaNumeros()= 0 - -17.777
                        10 - -12.222
                        20 - -6.666
    """
    x=0
    print("F - C")
    while x<=120:
        print(x,"-",(x-32)*5/9)
        x=x+10

farCel()
