#Bibliotecas
import random
import string
import os #executar somente en linux
#instalar biblioteca pytest

#Finalizada
def menu():
    #Representamos millas, pies, pulgadas y metros como números
 #convierteAMetros: Float -> Float -> Float -> Float
 #El primer parámetro representa una longitud en millas,
 #el segundo en pies, el tercero en pulgadas y, el valor de
 #retorno representa su equivalente en metros.
 #entrada: 1, 0, 0; salida: 1609.344
 #entrada: 0, 1, 0; salida: 0.3048
 #entrada: 0, 0, 1; salida: 0.0254
 #entrada: 1, 1, 1; salida: 1609.6742
    numJugadores = 2
    opcion = 0
    while(opcion!=3):
        os.system('clear')
        print('\nTUTTI FRUTTI')
        print('\n',numJugadores,' Jugadores')
        print('\n[1] Cambiar Cantidad de Jugadores')
        print('[2] Jugar')
        print('[3] Salir')
        try:
            opcion=int(input("Selecione una opcion: "))
        except:
            menu()
            pass
        if(opcion==1):
            numJugadores = cambiaNumeroJugadores()
        if(opcion==2):
            jugar(numJugadores)
        if(opcion==3):
            quit()





def jugar(numJugadores):
    listaPuntos = [0] * numJugadores
    print(listaPuntos)
    listaLetras = []

    #if(0==0):
    while(max(listaPuntos)<200):
        os.system('clear')

        #Elige la letra para la rodada
        letra = eligeLetra(listaLetras)
        listaLetras.append(letra)

        #Popula los campos de la matriz de la rodada
        matrizPalabras = populaMatriz(numJugadores)

        #Imprime la matriz de la rodada
        imprimeMatriz(matrizPalabras,numJugadores)

        #Conta los puntos de cada jugador
        listaPuntos = contarPuntos(matrizPalabras,numJugadores,letra)

        #Imprime la lista de puntos
        for jugador in range(0,numJugadores):
            print('JUGADOR ', jugador+1,listaPuntos[jugador],' puntos')

        input()

    #Comando para el ganador:
    for jugador in range(0,numJugadores):
        if(listaPuntos[jugador] >= 200):
            print('Jugador ',jugador,' ganou!')
            input('Precione Enter para finalizar')


#testes
def contarPuntos(matrizPalabras,numJugadores,letra):
    listaPuntos = [0] * numJugadores
    #Contagen de los puntos de cada jugadores
    for jugador in range(0,numJugadores):
        for numCategoria in range(7):
            #Palabras con la letra incorecta
            if(letra == matrizPalabras[numCategoria][jugador][0].upper()):
                matrizPalabras[numCategoria][jugador] = ''
            #Exclue palabras no completadas
            if(matrizPalabras[numCategoria][jugador] != ''):
                #Conta las palabras iguales
                contPalIguales = 0
                #Verifica si sólo un jugador tiene palabras
                palabraSola = True

                for jugadorComp in range(0,numJugadores):
                    if(matrizPalabras[numCategoria][jugador] == matrizPalabras[numCategoria][jugadorComp]) and (jugador != jugadorComp):
                        contPalIguales = contPalIguales + 1
                    if (jugador != jugadorComp) and (matrizPalabras[numCategoria][jugadorComp] != ''):
                        palabraSola = False

                if(palabraSola == True):
                    listaPuntos[jugador] = listaPuntos[jugador] + 20
                else:
                    if(contPalIguales == 0):
                        listaPuntos[jugador] = listaPuntos[jugador] + 10
                    else:
                        listaPuntos[jugador] = listaPuntos[jugador] + 5

    return listaPuntos

def test_contarPuntos():
    #Función de prueba de la función fmaximo
    assert fmaximo(3,4) == 4
    assert fmaximo(-4,92) == 92
    assert fmaximo(-10,2) == 2
    assert fmaximo(-5,72) == 72

#Finalizada (cambiar hola)
def populaMatriz(numJugadores):
    #Crea la matriz de jugadores X categorias para cada rodada
    matrizPalabras = [['' for i in range(0,numJugadores)] for j in range(0,7)]

    #Pregunta las palabras para cada jugador
    for jugador in range(0,numJugadores):
        #Imprime cual es el jugador
        print('\nJUGADOR ',jugador+1)
        for numCategoria in range(0,7):
            #Recibe la palabra del jugador
            #matrizPalabras[numCategoria][jugador] = recibePalabra(numCategoria)
            matrizPalabras[numCategoria][jugador] = 'hola'
    return matrizPalabras

def test_populaMatriz():
    #Función de prueba de la función fmaximo
    assert fmaximo(3,4) == 4
    assert fmaximo(-4,92) == 92
    assert fmaximo(-10,2) == 2
    assert fmaximo(-5,72) == 72


#Finalizada
def imprimeMatriz(matrizPalabras,numJugadores):
    #Imprime la matriz
    #os.system('clear')
    for jugador in range(0,numJugadores):
        #Imprime cual es el jugador
        print('\nJUGADOR ',jugador+1)
        for numCategoria in range(0,7):
            #Recibe la palabra del jugador
            print('\n',matrizPalabras[numCategoria][jugador])

#Finalizada
def cambiaNumeroJugadores():
    numJugadores=2
    try:
        numJugadores = int(input('\nIngrese la cantidad de jugadores[2,3,4,5]: '))
        if(numJugadores<2)or(numJugadores>5):
            print('\nCantidad invalida!')
            return cambiaNumeroJugadores()
    except:
        print('\nCantidad invalida!')
        return cambiaNumeroJugadores()
        pass
    return numJugadores

def test_cambiaNumeroJugadores():
    #Función de prueba de la función fmaximo
    assert fmaximo(3,4) == 4
    assert fmaximo(-4,92) == 92
    assert fmaximo(-10,2) == 2
    assert fmaximo(-5,72) == 72


#Finalizada
def eligeLetra(listaLetrasAnteriores):
    nuevaLetra = random.choice(string.ascii_uppercase)
    repetida = False
    for letraAnterior in (listaLetrasAnteriores):
        if(letraAnterior == nuevaLetra):
            repetida = True
    if(repetida == False):
        print('\nLa letra es: ',nuevaLetra)
        return nuevaLetra

def test_eligeLetra():
    #Función de prueba de la función fmaximo
    assert fmaximo(3,4) == 4
    assert fmaximo(-4,92) == 92
    assert fmaximo(-10,2) == 2
    assert fmaximo(-5,72) == 72


#Finalizada
def recibePalabra(numCategoria):
    if(numCategoria==0):
        txtCategoria = 'Ingrese el nombre de una persona: '
    if(numCategoria==1):
        txtCategoria = 'Ingrese una color: '
    if(numCategoria==2):
        txtCategoria = 'Ingrese un animal: '
    if(numCategoria==3):
        txtCategoria = 'Ingrese una comida: '
    if(numCategoria==4):
        txtCategoria = 'Ingrese una flor: '
    if(numCategoria==5):
        txtCategoria = 'Ingrese una fruta: '
    if(numCategoria==6):
        txtCategoria = 'Ingrese un pais: '
    return input(txtCategoria)

def test_contarPuntos():
    #Función de prueba de la función fmaximo
    assert fmaximo(3,4) == 4
    assert fmaximo(-4,92) == 92
    assert fmaximo(-10,2) == 2
    assert fmaximo(-5,72) == 72




menu()#llamada del juego en el terminal
