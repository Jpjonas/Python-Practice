#Bibliotecas
import random
import string
import os #executar somente en linux
#instalar biblioteca pytest

#Finalizada
def menu():
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

    if(0==0):
    #while(max(listaPuntos)<200):
        os.system('clear')

        #Elige la letra para la rodada
        letra = eligeLetra(listaLetras)
        listaLetras.append(letra)

        #Popula los campos de la matriz de la rodada
        matrizPalabras = populaMatriz(numJugadores)

        #Imprime la matriz de la rodada
        imprimeMatriz(matrizPalabras,numJugadores)

        #Conta los puntos de cada jugador
        listaPuntos = contarPuntos(matrizPalabras,numJugadores)

    #Comando para el ganador:
    #...


def contarPuntos(matrizPalabras,numJugadores):#contagen de los puntos
    listaPuntos=[]
    #Contagen de los puntos de cada jugadores
    #Sumando los puntos obtenidos antes
    for jugador in range(0,numJugadores):
        for numCategoria in range(7):
            for jugadorComp in range(0,numJugadores):
                if(matrizPalabras[numCategoria][jugador] == matrizPalabras[numCategoria][jugadorComp]):
                    print("a")

    return listaPuntos


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

    input('Enter pra continuar')

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



menu()#llamada del juego en el terminal
