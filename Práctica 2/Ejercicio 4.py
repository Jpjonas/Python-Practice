def factoriales():
    """
    Representación de los datos:
    Representamos factoriales con números

    Signatura:
    contaNumeros: void -> void

    Declaracion de propósito:
    La función calcula y imprime el cálculo factorial .

    Ejemplos:
    >>> contaNumeros() 2 5 6={120,720}
    >>> contaNumeros() 1 4={20}
    """
    m=int(input("Ingrese la cantidad de factoriales: "))
    for x in range(0,m):
        n=int(input("Ingresse un valor para el calculo factorial: "))
        t=1 #Resultado del factorial
        for y in range(1,n+1):
            t=t*y
        print(t)

factoriales()
