def testaEntero():
    """
    Representación de los datos:
    Representamos números como datos

    Signatura:
    contaNumeros: void -> void

    Declaracion de propósito:
    La función testa si el usuario digita

    Ejemplos:
    >>> testaEntero() 1: Es un entero
    >>> testaEntero() b: no es un entero
    >>> testaEntero() -1: No es positivo
    """
    m=False
    while(m==False):
        try:
            a=int(input("Digite un número entero: "))
            if(a>=0):
                m=True
            else:
                print("No es positivo")
            print("Es un entero")
        except:
            print("No es un entero.")
            pass

testaEntero()
