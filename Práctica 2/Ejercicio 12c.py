def login():
    """
    Representación de los datos:
    Representamos contraseñas con números

    Signatura:
    contaNumeros: void -> boolean
    Devuelve si el usuario ingresso la contraseña correcta

    Declaracion de propósito:
    La función contiene una contraseña inventada,
    y compara con la contraseña ingressada 3 veces.

    Ejemplos:
    >>> login() "abc123" "123abc" "holamundo"
    >>> login() "holamundo"
    >>> login() "asdasd" "holamundo"
    """
    c="holamundo"
    x=""
    t=0
    while(c!=x)and(t<3):
        x=input("Ingresse la contraseña: ")
        t=t+1

    if(t<3):
        return(True)
    else:
        return(False)

login()
