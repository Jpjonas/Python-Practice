#Jonas Pollnow
#Programacion 2

import random
import string
import os
import pytest

#Para windows cambiar:
    #os.system('clear')
#Por:
    #os.system('cls')

def menu():
    #Representacion de los datos:
    #Representamos opciones del juego como numeros

    #Signatura:
    #menu: No posee -> No posee

    #Declaracion de proposito:
    #La funcion imprime las opciones del juego en la pantalla,
    #recibe la entrada del usuario y llama la funcion correspondente

    #Ejemplos:
    #>>> menu() 1 -> cambiaNumeroJugadores()
    #>>> menu() 2 -> jugar(numJugadores)
    #>>> menu() 3 -> quit()

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
    #Representacion de los datos:
    #Representamos jugadores, categorias y puntos como numeros

    #Signatura:
    #jugar: int -> No posee

    #Declaracion de proposito:
    #La funcion llama las otras funciones segun la estructura del juego,
    #imprime los puntos y reconoce el ganador del juego

    #Ejemplos:
    #>>> jugar(2) -> No posee
    #>>> jugar(3) -> No posee
    #>>> jugar(5) -> No posee

    listaPuntos = [0] * numJugadores
    listaLetras = []
    while(max(listaPuntos)<200):
        os.system('clear')
        #Elige la letra para la rodada
        letra = eligeLetra(listaLetras)
        listaLetras.append(letra)
        #Llena los campos de la matriz de la rodada
        matrizPalabras = llenaMatriz(numJugadores)
        #Conta los puntos de cada jugador
        listaPuntos = contarPuntos(matrizPalabras,numJugadores,letra,listaPuntos)
        #Imprime la matriz de la rodada
        os.system('clear')
        print('\n'.join(['      '.join(['{:4}'.format(palabra) for palabra in linea]) for linea in matrizPalabras]))
        #Imprime la lista de puntos
        for jugador in range(0,numJugadores):
            print('\nJUGADOR ', jugador+1,': ',listaPuntos[jugador],' puntos')
        input('\nPrecione Enter para continuar')
    #Imprime el ganador
    for jugador in range(0,numJugadores):
        if(listaPuntos[jugador] >= 200):
            print('\nJUGADOR ',jugador+1,' ganou!')
    input('\nPrecione Enter para finalizar')

def contarPuntos(matrizPalabras,numJugadores,letra,listaPuntos):
    #Representacion de los datos:
    #Representamos jugadores, categorias y puntos como numeros
    #Y palabras como string

    #Signatura:
    #contarPuntos: list(of list(of string)) -> int -> string -> list(of int)
    #Recibe la matriz de palavras, el numero de jugadores, la letra de la ronda, y la lista de puntos de los jugadores
    #Devuelve la lista Puntos de los jugadores

    #Declaracion de proposito:
    #La funcion conta los puntos de cada jugador en la ronda con las reglas:
    # *Para las palabras validas escritas en una categoria y escritas solamente por un jugadorse asignaran 10 puntos
    # *Para las palabras repetidas se asignaran 5 puntos
    # *Para las palabras no validas o categorias no completadas con una palabra, los participantes no obtendran ninguna puntuacion
    # *En caso de ser unicamente un jugador quien pudo encontrar una palabra conla letra de dicho turno, se le asignaran 20 puntos

    for jugador in range(0,numJugadores):
        for numCategoria in range(7):
            #Palabras nulas
            if(matrizPalabras[numCategoria][jugador] == ''):
                matrizPalabras[numCategoria][jugador] = ' '
            else:
                #Palabras con la letra incorecta
                if(letra != matrizPalabras[numCategoria][jugador][0].upper()):
                    matrizPalabras[numCategoria][jugador] = ' '
            #Verifica palabras iguales del mismo jugador
            for numCategoriaComp in range(0,7):
                if(numCategoria != numCategoriaComp) and (matrizPalabras[numCategoria][jugador] == matrizPalabras[numCategoriaComp][jugador]):
                    matrizPalabras[numCategoriaComp][jugador] = ' '
    #Contagen de los puntos
    for jugador in range(0,numJugadores):
        for numCategoria in range(7):
            if(matrizPalabras[numCategoria][jugador] != ' '):
                #Conta las palabras iguales
                contPalIguales = 0
                #Verifica si solo un jugador tiene palabras
                palabraSola = True
                #Compara con las palabras de los otros jugadores
                for jugadorComp in range(0,numJugadores):
                    if(matrizPalabras[numCategoria][jugador].upper() == matrizPalabras[numCategoria][jugadorComp].upper()) and (jugador != jugadorComp):
                        contPalIguales = contPalIguales + 1
                    if (jugador != jugadorComp) and (matrizPalabras[numCategoria][jugadorComp] != ' '):
                        palabraSola = False
                #Suma los puntos
                if(palabraSola == True):
                    listaPuntos[jugador] = listaPuntos[jugador] + 20
                else:
                    if(contPalIguales == 0):
                        listaPuntos[jugador] = listaPuntos[jugador] + 10
                    else:
                        listaPuntos[jugador] = listaPuntos[jugador] + 5
    return listaPuntos

def llenaMatriz(numJugadores):
    #Representacion de los datos:
    #Representamos jugadores, categorias y puntos como numeros

    #Signatura:
    #llenaMatriz: int -> list(of list(of string))
    #Recibe la cantidad de jugadores y devuelve la matriz con las palabras de cada jugador

    #Declaracion de proposito:
    #La funcion crea la matriz de jugadores X categorias y define las palabras para cada posicion

    #Ejemplos:
    #>>> llenaMatriz(2) -> [['Jonas','Jon'],['',''],['jirafa','jirafa'],['jamon','jamon'],['',''],['',''],['Jamaica','']]
    #>>> llenaMatriz(2) -> [['Antonio','Ana'],['azul','azul'],['anaconda',''],['arroz','arroz'],['',''],['',''],['Argentina','Alemania']]
    #>>> llenaMatriz(2) -> [['Carlos',''],['celeste',''],['','caballo'],['canelones',''],['camelia',''],['coco',''],['Colombia','China']]

    #Crea la matriz de jugadores X categorias para cada ronda
    matrizPalabras = [[' ' for i in range(0,numJugadores)] for j in range(0,7)]
    #Pregunta las palabras para cada jugador
    for jugador in range(0,numJugadores):
        #Imprime cual es el jugador
        print('\nJUGADOR ',jugador+1)
        for numCategoria in range(0,7):
            #Recibe la palabra del jugador
            matrizPalabras[numCategoria][jugador] = recibePalabra(numCategoria)
    return matrizPalabras

def cambiaNumeroJugadores():
    #Representacion de los datos:
    #Representamos jugadores como numeros

    #Signatura:
    #cambiaNumeroJugadores: No posee -> int
    #Devuelve la cantidad de jugadores

    #Declaracion de proposito:
    #La funcion recibe y verifica la nueva cantidad de jugadores

    #Ejemplos:
    #>>> cambiaNumeroJugadores()  3 -> 3
    #>>> cambiaNumeroJugadores()  2 -> 2
    #>>> cambiaNumeroJugadores()  5 -> 5

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

def eligeLetra(listaLetrasAnteriores):
    #Representacion de los datos:
    #Representamos letras como string

    #Signatura:
    #eligeLetra: list(of string) -> string
    #Recibe la lista de letras anteriores y devuelve una nueva letra aleatoria

    #Declaracion de proposito:
    #La funcion elige una nueva letra para la ronda

    #Ejemplos:
    #>>> eligeLetra(['F','G','T']) -> 'R'
    #>>> eligeLetra([]) -> 'A'
    #>>> eligeLetra(['Q','L']) -> 'T'

    nuevaLetra = random.choice(string.ascii_uppercase)
    repetida = False
    for letraAnterior in listaLetrasAnteriores:
        if(letraAnterior == nuevaLetra):
            repetida = True
    if(repetida == False):
        print('\nLa letra es: ',nuevaLetra)
        return nuevaLetra

def recibePalabra(numCategoria):
    #Representacion de los datos:
    #Representamos categorias com numeros

    #Signatura:
    #recibePalabra: int -> string
    #Recibe el numero de la categoria
    #y devuelve la palabra ingresada por el jugador para dicha categoria

    #Declaracion de proposito:
    #La funcion convierte el numero de la categoria para el texto de input
    #y recibe la palabra ingresada por el jugador

    #Ejemplos:
    #>>> recibePalabra(0)  'Jonas' -> 'Jonas'
    #>>> recibePalabra(3)  'Manzana' -> 'Manzana'
    #>>> recibePalabra(6)  'Alemania' -> 'Alemania'

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
    #Funcion de prueba de la funcion contarPuntos
    assert contarPuntos([['Jonas','Jon'],['',''],['jirafa','jirafa'],['jamon','jamon'],['',''],['',''],['Jamaica','']],2,'J',[110,55]) == [150,75]
    assert contarPuntos([['Antonio','Ana'],['azul','azul'],['anaconda',''],['arroz','arroz'],['',''],['',''],['Argentina','Alemania']],2,'A',[0,0]) == [50,30]
    assert contarPuntos([['Carlos',''],['celeste',''],['','caballo'],['canelones',''],['camelia',''],['coco',''],['Colombia','China']],2,'C',[30,40]) == [140,70]

test_contarPuntos()#llamada de la funcion de teste

menu()#llamada del juego en el terminal
