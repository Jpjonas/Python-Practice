def promedioNotas():
    """
    Representación de los datos:
    Representamos notas con números

    Signatura:
    contaNumeros: void -> void

    Declaracion de propósito:
    La función recie varias notas y calcula el promedio

    Ejemplos:
    >>> promedioNotas() 7 8=7,5
    >>> promedioNotas() 6=6
    >>> promedioNotas() 5 8 9=7,5
    """
    r="si"
    t=0
    c=0
    while(r=="si"):
        n=int(input("Digite la nota: "))
        t=t+n
        c=c+1
        r=input("Desea ingresar mas notas?(si/no)")
    print("Promedio: ",t/c)

promedioNotas()
