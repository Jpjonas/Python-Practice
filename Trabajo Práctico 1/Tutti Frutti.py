#Bibliotecas
import random
import string
import os
import numpy as np
#intalar biblioteca numpy
#instalar biblioteca pytest


def menu():
    numJugadores = 2
    opcion = 0
    while(opcion!=3):
        os.system('clear')
        print '\nTUTTI FRUTTI'
        print '\n',numJugadores,' Jugadores'
        print '\n[1] Cantidad de Jugadores'
        print '[2] Jugar'
        print '[3] Salir'
        opcion=int(input("Selecione una opcion: "))
        if(opcion==1):
            numJugadores = cambiaNumeroJugadores()
        if(opcion==2):
            jugar(numJugadores)
        if(opcion==3):
            quit()


def cambiaNumeroJugadores():
    numJugadores=2
    try:
        numJugadores = int(input('\nIngrese la cantidad de jugadores[1,2,3,4,5]: '))
        if(numJugadores<1)or(numJugadores>5):
            print '\nCantidad invalida!'
            return cambiaNumeroJugadores()
    except:
        print '\nCantidad invalida!'
        return cambiaNumeroJugadores()
        pass
    return numJugadores


def jugar(numJugadores):
    letra = random.choice(string.ascii_uppercase)
    print '\nLa letra es: ',letra
    matrizPalavras = np.arange(7*numJugadores).reshape(numJugadores, 7)
    listaPuntos=[]
    for x in range(0,numJugadores):
        print "\nJUGADOR ",x
        linea=[]
        for y in range(0,7):
            linea.append(recibePalabra(y))
        matrizPalavras.append(linea)
    contaPuntos(matrizPalavras)
    print(matrizPalavras)


def recibePalabra(numCategoria):
    txtCategoria=""
    if(numCategoria==0):
        txtCategoria="Ingrese el nombre de uma persona: "
    if(numCategoria==1):
        txtCategoria="Ingrese una color: "
    if(numCategoria==2):
        txtCategoria="Ingrese un animal: "
    if(numCategoria==3):
        txtCategoria="Ingrese una comida: "
    if(numCategoria==4):
        txtCategoria="Ingrese una flor: "
    if(numCategoria==5):
        txtCategoria="Ingrese una fruta: "
    if(numCategoria==6):
        txtCategoria="Ingrese un pais: "
    palabra = input(txtCategoria)
    return palabra


def contaPuntos(matrizPalavras):#contagen de los puntos
    listaPuntos=[]
    #Contagen de los puntos de cada jugadores
    #Sumando los puntos obtenidos antes
    for x in range(matrizPalavras):
        for y in range(x):
            for i in range(matrizPalavras):
                for j in range(i):
                    #if(matrizPalavras[][]==matrizPalavras[][])
                    print("a")
    return listaPuntos


menu()#llamada del juego en el terminal
