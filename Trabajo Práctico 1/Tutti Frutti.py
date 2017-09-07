#bibliotecas
import random
import string



def main():
    # Número de jugadores
    n=int(input("Ingrese la cantidad de jugadores[2,3,4,5]: "))
    # Letra generada al azar
    l=random.choice(string.ascii_letters)
    for(j in range(1,n)):
