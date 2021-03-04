
import random 
#----entrada----#
mensajesaludo = """
    bienvenido
        a este progrma 
    ¡¡¡juguemos!!!"""
preguntanumero = '''
    en este juego debes asertar un nuemro entero
    que va desde el 1-10, la idea es que 
    lo puedas intentar antes de que se te acaben las 
    vidas...
    muchos exitos, ingresa tu numero 
'''
preguntafallo = "fallaste, intenta de nuevo"
mensajeganaste = "ganaste, gracias por jugar"
mensajeperdiste = "has perdido, vuelve a comenzr"
#----entrada al codigo-----#
numerooculto = random.randint (1,10)
vidas = 5
numeroingresado = int (input (preguntanumero))
while (numeroingresado != numerooculto and vidas >1):
    vidas -=1
    print (f'te quedan {vidas} vidas')
    print (numerooculto)
    numeroingresado = int (input(preguntafallo))

if (vidas >=0 and numeroingresado == numerooculto):
    print (mensajeganaste)
else :
    print (mensajeperdiste, "El numero era el", numerooculto)
