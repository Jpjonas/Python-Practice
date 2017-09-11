#Bibliotecas
import random
import string
import pprint

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
    #verificar si é um número y si esta dentro do possivel
    return int(input("Ingrese la cantidad de jugadores[1,2,3,4,5]: "))


#n->Número de jugadores
def jugar(n):
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
        #verificar si la pontuacion es mayor que 200

    #Loops para ingresar las palabras de cada letra
    for x in range(0,n):
        print("\nJUGADOR ",x)
        linea=[]
        for y in range(0,7):
            t="0" #Caracter que no es una letra
            while(t[0].upper()!=l): #Verificacion de la letra inicial de la palabra ingresada
                t=input("Ingresse la palabra: ")
            linea.append(t)
        matrizPalavras.append(linea)


    #impresion de la matriz(verificar)
    pprint.pprint(matriz)

def contaPuntos(matrizPalavras):
    listaPuntos=[]
    ##Contagen de los puntos de cada jugadores
    #Sumando los puntos otenidos antes

    return listaPuntos



#Llamada del juego en el terminal
menu()
