# -*- encoding: utf-8 -*-

# Importación de librerias (si las hubiese) una por línea.

def nombre_de_la_funcion(argumento1, argumento2):
    """
	Representación de los datos ¿Cómo se representa cada tipo de 
	dato?
	Signatura:
        nombre_de_la_funcon : tipo_argumento1 -> tipo_argumento2 -> tipo_valor_retorno
        
	Declaración de propósito. ¿Qué hace la función 'nombre_de_la_funcion'?

	Ejemplos:
	>>> nombre_de_la_funcion(arg1, arg2) = ret1
        >>> nombre_de_la_funcion(arg3, arg4) = ret2
        >>> nombre_de_la_funcion(arg5, arg6) = ret3
    """
    print('primer linea de código')
    print('segunda linea de código')
    # Comentario dentro del código explicando el funcionamiento
    # de un bloque de código como el siguiente (si se cree necesario)
    for x in range(1,5):
        print(x)

    return 'valor de retorno'


# La siguiente línea indica la acción que se realizará
# al llamar el archivo desde la terminal o desde IDLE (no es obligatoria).
nombre_de_la_funcion('argumento1','argumento2')
