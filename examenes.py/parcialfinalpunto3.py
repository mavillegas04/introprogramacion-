# Se sabe que un Dólar son 0.82 euros, indique a un usuario que ingrese su
# dinero en dólares y su nombre, luego muestre en pantalla el nombre del usuario y cuanto
# dinero tiene en dólares (recuerde validar que todos los datos ingresados por el usuario sean
# del formato correcto)

def conversionEuros ():
    iscorrectinfo = False 
    while (iscorrectinfo == False): 
        try: 
            nombre = input ('cual es su nombre: ')
            assert (nombre.isalpha())
            iscorrectinfo = True
        except AssertionError: 
            print ('dato no valido, inenta de nuevo')
    iscorrectinfo = False
    while (iscorrectinfo == False):
        try: 
            dinero = float (input('ingrese una cantidad de dinero en dolares'))
            iscorrectinfo = True
        except ValueError:
            print ('dato no valido, intenta de nuevo')

    print (f'hola {nombre}, la cantidad de dinero en euros es {dinero*0.82}')
conversionEuros()
input ('\nPresione una tecla para continuar')
