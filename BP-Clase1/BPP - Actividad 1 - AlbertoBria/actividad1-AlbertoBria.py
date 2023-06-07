


file = 'prueba.txt'


class MiExcepcion(Exception):
    def __init__(self):
        super().__init__('El número es mayor que 10')


def pedir_numero():

    try: 
        numero = int(input('Introduzca un número: '))

        if numero > 10:
            raise MiExcepcion
        
        elif numero == 0000:
            pass

        else:
            print('El número introducido es: ',numero)
        
    except ValueError as e:
        print('Value error', e)

    except TypeError as e:
        print('TypeError', e)


def abrir_archivo(file):
    try: 
        with open(file,'r') as f: 
           print(f.read())
    
    except FileNotFoundError:
        print('Archivo no encontrado')
    
    except IOError:
        print('Error trabajando con el archivo')

    except Exception as e:
        print('Error inesperado',e)

    finally: 
        f.close()



while True:

    print('Punto 1 del ejercicio, PEDIR NÚMERO')
    pedir_numero()

    print('Punto dos del ejercicio, LEER ARCHIVO')
    abrir_archivo(file)
