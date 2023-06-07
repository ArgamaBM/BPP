def solicitar_numero():
    """
    Solicita al usuario un número y se asegura de que sea positivo.

    Returns:
        int: El número ingresado por el usuario, transformado a su valor absoluto.
    """
    n = abs(int(input('Introduzca un número: ')))
    return n


def imprimir_cuenta(n):
    """
    Imprime una cuenta del 0 al número ingresado por el usuario.

    Args:
        n (int): El número ingresado por el usuario.
    """
    print(f'Cuenta del 0 al {n}: ')
    for i in range(0, n+1):
        print(i)


def generar_diccionario(n):
    """
    Genera un diccionario utilizando operaciones matemáticas en un rango de 0 al número ingresado.

    Args:
        n (int): El número ingresado por el usuario.

    Returns:
        dict: El diccionario creado con las claves y valores generados.
    """
    dictionary = {}
    valores = [x**6 for x in range(n)]
    claves = [y**3 for y in range(n)]

    for c in range(0, n):
        valor = valores[c]
        clave = claves[c]
        dict1 = {clave: valor}
        dictionary.update(dict1)

    return dictionary


def imprimir_resultados(dictionary):
    """
    Imprime el diccionario creado y los pares clave/valor del diccionario.

    Args:
        dictionary (dict): El diccionario creado.
    """
    print(f'Diccionario creado: {dictionary}')

    print(f'Pares Clave/Valor: ')
    for x, y in dictionary.items():
        print(f'Clave: {x} / Valor: {y}')


# Obtener el número del usuario
numero = solicitar_numero()

# Imprimir la cuenta del 0 al número
imprimir_cuenta(numero)

# Generar el diccionario
diccionario = generar_diccionario(numero)

# Imprimir los resultados
imprimir_resultados(diccionario)