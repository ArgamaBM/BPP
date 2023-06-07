# Solicitar al usuario un número y asegurarse de que sea positivo
n = abs(int(input('Introduzca un número: ')))

# Imprimir una cuenta del 0 al número ingresado por el usuario
print(f'Cuenta del 0 al {n}: ')
for i in range(0, n+1):
    print(i)

# Crear un diccionario vacío
dictionary = {}

# Generar listas de valores y claves utilizando operaciones matemáticas en un rango de 0 al número ingresado
valores = [x**6 for x in range(n)]
claves = [y**3 for y in range(n)]

# Iterar sobre los índices del rango de 0 al número ingresado
for c in range(0, n):
    # Obtener el valor y la clave correspondientes a cada índice
    valor = valores[c]
    clave = claves[c]
    
    # Crear un diccionario temporal con la clave y el valor, y luego actualizar el diccionario principal
    dict1 = {clave: valor}
    dictionary.update(dict1)

# Imprimir el diccionario creado
print(f'Diccionario creado: {dictionary}')

# Imprimir los pares clave/valor del diccionario
print(f'Pares Clave/Valor: ')
for x, y in dictionary.items():
    print(f'Clave: {x} / Valor: {y}')