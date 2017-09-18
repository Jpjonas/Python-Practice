def fmaximo(x, y):
    #comentario teste
    if x > y:
        return x
    else:
        return y

def test_fmaximo():
    assert fmaximo(3,4) == 4
    assert fmaximo(-4,92) == 92
    assert fmaximo(-10,2) == 2
    assert fmaximo(-5,72) == 72
