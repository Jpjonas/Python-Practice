def login():
    """
    Representación de los datos:
    Representamos contraseñas con números

    Signatura:
    contaNumeros: void -> void

    Declaracion de propósito:
    La función contiene una contraseña inventada,
    y compara con la contraseña ingressada.

    Ejemplos:
    >>> login() "abc123" "123abc" "holamundo"
    >>> login() "holamundo"
    >>> login() "asdasd" "holamundo"
    """
    c="holamundo"
    x=""
    while(c!=x):
        x=input("Ingresse la contraseña: ")


login()
