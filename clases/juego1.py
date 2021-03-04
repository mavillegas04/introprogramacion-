#-----entradas-----#
MENSAJESALUDO = 'bienvenido a este juego, comencemos'
PREGUNTANUMERO = '''
        en este juego debes acertar el numero 
        que va desde el 1 - 10 la idea es que 
        lo puedes inetentar las veces que quieras...
        muchos exitos, 
        comencemos ingresa el numero
'''
PREGUNTAFALLO = 'haz fallado, vuelve a intentarlo, pon otro numero'
MENSAJEGANASTE= 'felicidades lo lograste'
MENSAJEPERDISTE = 'haz perdido, lo siento'

#-----ingresa el codigo-----#
numerooculto = 7
vidas = 5
print (MENSAJESALUDO)
numeroingresado = int (input (PREGUNTANUMERO))
if (numeroingresado != numerooculto):
    vidas -=1
while (numerooculto != numeroingresado and vidas >0):
    numeroingresado = int (input(PREGUNTAFALLO))
    vidas -=1

if (vidas >=0 and numerooculto == numeroingresado):
    print (MENSAJEGANASTE)
    print (vidas)
else:
    print (MENSAJEPERDISTE, 'el numero correcto era', numerooculto)