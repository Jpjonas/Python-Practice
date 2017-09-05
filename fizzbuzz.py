# -*- encoding: utf-8 -*-

# Diferentes 

# FizzBuzz, el enfoque "directo"
def fizzbuzz1():
    """
     Imprime los números del 1 al 100.
     Para múltiplos de tres imprima "Fizz" en lugar del número
     y en lugar de los múltiplos de cinco imprima "Buzz"
     Si es múltiplo de ambos, imprime "FizzBuzz"
     args:
        No posee
     returns:
        No posee
    """
    for num in range(1,101):
        # Para verificar que un número es múltpilo de otro, verficamos
        # si el resto de dividir uno por otro es igual a cero
        if num % 3 == 0 and num % 5 == 0:
        # En lugar de la línea anterior ,
        # podríamos utilizar la siguiente condición
        # if num % 15 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

# Otra opción, "concatenamos" en una variable la solución
def num_2_fizzbuzz(numero):
    """
        Devuelve (¡Ojo! No imprime, devuelve) el valor a imprimir
        para el juego FizzBuzz correspondiente a un número.
        Args:
            numero: argumento de tipo entero que representa el número
                    para el que se debe calcular su valor.
        Returns:
            returns: la función retorna el valor correspondiente al argumento
                    dado para el juego FizzBuzz
    """
    ret = ''
    if numero%3 == 0:
        # Si el número es múltipo de 3,
        # CONCATENAMOS a la solución la palabra 'Fizz'
        ret = ret + 'Fizz'
    if numero%5 == 0:
        # Si el número es múltipo de 5,
        # CONCATENAMOS a la solución la palabra 'Buzz'
        ret = ret + 'Buzz'
    if ret == '':
        # Si el número no era múltiplo de 3 ni de 5,
        # la variable ret no fue modificada
        ret = str(numero)
    return ret

def fizzbuzz2():
    """
     Itera sobre los números del 1 al 100.
     En cada itereación, se obtiene el valor correspondiente
     a cada número en el juego FizzBuzz utilizando la función
     'num_2_fizzbuzz'
     args:
        No posee
     returns:
        No posee
    """
    for x in range(1,101):
        valor_correspondiente = num_2_fizzbuzz(x)
        print(valor_correspondiente)


# Una solución un poco más oscura y enigmática...
# Esta solución es para mostrar características particulares
# del lenguaje Python, pero escapa a los alcances del curso
def fizzbuzz3():
    """
     Imprime los números del 1 al 100.
     Para múltiplos de tres imprime "Fizz" en lugar del número
     y en lugar de los múltiplos de cinco imprime "Buzz"
     Si es múltiplo de ambos, imprime "FizzBuzz"
     args:
        No posee
     returns:
        No posee
    """
    for i in range(1,101):
        print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)
