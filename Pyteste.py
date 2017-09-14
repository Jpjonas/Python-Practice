def fmaximo(x, y):
    ’’’
    Función que determina el máximo entre dos números.
    Args:
    x: Argumento de tipo numérico a comparar con el segundo ←-
    argumento.
    y: Argumento de tipo numérico a comparar con el primer ←-
    argumento.
    Returns:
    La función retorna el mayor de sus argumentos
    ’’’
    if x > y:
        return x
    else:
        return y

def test_fmaximo():
    ’’’
    Función de prueba de la función fmaximo
    ’’’
    assert fmaximo(3,4) == 4
    assert fmaximo(-4,92) == 92
    assert fmaximo(-10,2) == 2
    assert fmaximo(-5,72) == 72
