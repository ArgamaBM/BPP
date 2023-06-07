
# Actividad_4

#Punto 1: 
my_list = [[4,78,3],[1,2,3,4,5,6,7,8],[323,456,200]]

for l in my_list:
    maximo = max(l)
    print(f'El número más alto de esta sublista: {l} es: {maximo}')

'''
En primer lugar, se ha diseñado el programa con la mayor sencillez 
y eficiencia posible. Se ha añadido la variable máximo (la cual puede obviarse) para
mayor claridad del ejercicio. 

Este programa declara una lista de listas, donde se añade a cada sublista 
una serie de numeros enteros aleatorios.

Con un bucle for, se iteran cada una de las sublistas y, empleando la función 
integrada max() y print(), este bucle devolverá el valor numérico máximo de
cada sublista.

Empleando el debugger integrado en VSCode y añadiendo un punto de interrupción 
en la línea 9 de código (¨print(f'El numero mas alto de esta lista: {l} es {max(l)}')¨),
podemos controlar qué está sucediendo en el programa.

Al ejecutar el programa en modo debug, los resultados obtenidos son los mostrados a 
continuación (nos centraremos en ¨locals¨(variables locales) y ¨function variables¨
(variables de uso local)):

Primera ejecución:
    - l:[4,78,3] -> nos muestra, en la primera ejecución del bucle for, el valor que toma
    la variable l, en este caso el de la sublista 0. 
    - En el desglose de la variable l, nos muestra los elementos iterados y la longitud 
    de la sublista, en este caso 3. 
    - máximo: 78 -> es la variable donde se almacena el valor máximo de cada sublista.

Segunda ejecución:
    - l:[1,2,3,4,5,6,7,8] -> nos muestra, en la segunda ejecución del bucle for, el valor que toma
    la variable l, en este caso el de la sublista 1. 
    - En el desglose de la variable l, nos muestra los elementos iterados y la longitud 
    de la sublista, en este caso 8. 
    - máximo: 8 -> es la variable donde se almacena el valor máximo de cada sublista.

Tercera ejecución:
    - l:[323,456,200] -> nos muestra, en la tercera ejecución del bucle for, el valor que toma
    la variable l, en este caso el de la sublista 2. 
    - En el desglose de la variable l, nos muestra los elementos iterados y la longitud 
    de la sublista, en este caso 3. 
    - máximo: 456 -> es la variable donde se almacena el valor máximo de cada sublista. 

    Conclusión: el debug ha permitido controlar el flujo del programa, ayudando a identificar
    qué valores toma cada variable y como el programa está interpretando las líneas de código 
    descritas.
'''

#Punto 2

def is_prime(n):
    try:
        if n == 0 or n == 1:
            print ('No es primo')
        elif n == 2:
            print('Es primo')
        elif n%2 == 1:
            print('Es primo')
        else:
            print('No es primo')
    except ValueError as e:
        print(e,'Introduzca un caracter numerico entero positivo valido')

try:    
    n= int(input('Introduzca un numero: '))
    is_prime(n)
except ValueError as e:
    print(e,'Introduzca un caracter numerico entero positivo valido')
