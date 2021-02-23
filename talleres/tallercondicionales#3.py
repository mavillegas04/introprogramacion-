#-----constantes-----#
MENSAJEBIENVENIDA = "bienvenido, vamos a mirar cuantos años hay de diferencia"
PREGUNTAAÑOACTUAL = "en que año te encuentras actualmente :"
PREGUNTAOTROAÑO = "elige un año cualquiera y ponlo :"
MENSAJE = "{} {} años"
MENSAJEIGUALES = "no hay diferencia en los años elegidos"

#------entrada del codigo-----#
print (MENSAJEBIENVENIDA)
añoactual = int (input (PREGUNTAAÑOACTUAL))
otroaño = int (input (PREGUNTAOTROAÑO))
if (añoactual > otroaño) :
    resta = añoactual - otroaño
    print (MENSAJE . format ("han pasado" , resta))
elif (otroaño > añoactual) :
    resta = otroaño - añoactual
    print (MENSAJE . format ("faltan" , resta))
else :
    print (MENSAJEIGUALES)