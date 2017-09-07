def multiplos(a,b):
    """
    Representación de los datos:
    Representamos múltiplos como números

    Signatura:
    contaNumeros: int -> int -> int
    Los parametros representan números y devuelve la cantidad de múltiplos

    Declaracion de propósito:
    La función calcula la cantidad de multiplos de un número menores que el otro

    Ejemplos:
    >>> multiplos(10,8)=3
    >>> multiplos(64,50)=6
    >>> multiplos(20,15)=5
    """
    c=0
    for x in range(1,b):
        if(a%x==0):
            c=c+1
    return c

print(multiplos(10,8))
print(multiplos(64,50))
print(multiplos(20,15))
