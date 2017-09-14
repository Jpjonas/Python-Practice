#Bibliotecas
import random
import string
import pprint
import numpy as np

def menu():
    n=2 # Número de jugadores
    o=0
    while(o!=3):
        print("[1] Jugadores")
        print("[2] Jugar")
        print("[3] Salir")
        o=int(input("Selecione una opción: "))
        if(o==1):
            n=verificaJugadores()
        if(o==2):
            jugar(n)


def verificaJugadores():
    #verificar si é um número y si esta dentro do p6ossivel
    try:
        return int(input("Ingrese la cantidad de jugadores[1,2,3,4,5]: "))
    except:
        return verificaJugadores()
        pass


def jugar(n):#n->Número de jugadores
    # Letra generada al azar
    l=random.choice(string.ascii_uppercase)
    print("\nLa letra es: ",l)

    #Matriz de palavras de los jugadores
    matrizPalavras=[]
    #Lista de puntos de los jugadores
    listaPuntos=[]
    #Impresion de la lista de puntos de los jugadores
    for puntos in range(listaPuntos):
        pprint.pprint(listaPuntos)
        #Verificar si la pontuacion es mayor que 200

    #Loops para ingresar las palabras de cada letra
    for x in range(0,n):
        print("\nJUGADOR ",x)
        linea=[]
        for y in range(0,7):
            linea.append(recibePalabra(y))
        matrizPalavras.append(linea)

    contaPuntos(matriz)

    #Impresion de la matriz(verificar)
    pprint.pprint(matriz)


def recibePalabra(n):#n->la categoria conforme la posicion de la matriz
    c=""#Categorias
    if(n==0):
        c="Ingrese el nombre de uma persona: "
    if(n==1):
        c="Ingrese una color: "
    if(n==2):
        c="Ingrese un animal: "
    if(n==3):
        c="Ingrese una comida: "
    if(n==4):
        c="Ingrese una flor: "
    if(n==5):
        c="Ingrese una fruta: "
    if(n==6):
        c="Ingrese un país: "
    t=input(c)
    if(t[0].upper()!=l):#Verificacion de la letra inicial de la palabra ingresada
        t=""


def contaPuntos(matrizPalavras):#contagen de los puntos
    listaPuntos=[]
    #Contagen de los puntos de cada jugadores
    #Sumando los puntos obtenidos antes
    for x in range(matrizPalavras):
        for y in range(x):
            for i in range(matrizPalavras):
                for j in range(i):
                    print(a)


    return listaPuntos


menu()#llamada del juego en el terminal
