#Bibliotecas
import random
import string

def menu():
    n=1 # Número de jugadores
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

    matriz=[]
    for x in range(0,n):
        print("\nJUGADOR ",x)
        linea=[]
        for y in range(0,7):
            t="0"
            while(t[0].upper()!=l):
                t=input("Ingresse la ",...,": ")
            linea.append(t)
        matriz.append(linea)









menu()
