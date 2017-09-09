#Bibliotecas
import random
import string

def menu():
    n=1 # Número de jugadores
    o=0
    while(o!=3)
        print("[1] Jugadores")
        print("[2] Jugar")
        print("[3] Salir")
        o=int(input("Selecione una opción: "))
        if(o==1):
            n=verificaJugadores()
        if(0==2):
            jugar(n)

def verificaJugadores():
    #verificar si é um número y si esta dentro do possivel
    return int(input("Ingrese la cantidad de jugadores[1,2,3,4,5]: "))


#n->Número de jugadores
def jugar(n):
    # Letra generada al azar
    l=random.choice(string.ascii_letters)
    print("La letra es: ",l)

    matriz = [] # lista vacia
	for i in range(0,n):
        # cria a linea i
        linha = [] # lista vacia
	        for j in range(0,7):

            linha.append(input(""))

	        matriz.append(linha)





menu()
