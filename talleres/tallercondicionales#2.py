#-----constantes-----#
MENSAJEBIENVENIDA = "bienvenido, vamos a mirar como estas clasificado segun tu edad"
PREGUNTAEDAD = "cuantos años tienes? :"
MENSAJERESPUESTA = "estas clasifica cono un {}"
#-----entrada codigo-----"
print (MENSAJEBIENVENIDA)
edad = int (input (PREGUNTAEDAD))
if (edad < 18) :
    print (MENSAJERESPUESTA . format ("menor de edad, se un niño sano desde ya"))
elif (edad >= 18 and edad < 26) :
    print (MENSAJERESPUESTA . format ("joven, disfruta al maximo, tienes mucho por vivir y aprender"))
elif (edad >= 26 and edad < 61) :
    print (MENSAJERESPUESTA . format ("adulto, te queda mucho por vivir todavia"))
else :
    print (MENSAJERESPUESTA . format ("adulto mayor, tienes mucho que enseñar"))