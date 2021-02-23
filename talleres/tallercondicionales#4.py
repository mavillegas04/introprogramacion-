#-----constantes-----#
MENSAJEBIENVENIDA = "bienvenido, vamos a comenzar"
PREGUNTACENTIMETROS = "ingrese un numero de su eleccion en cm"
PREGUNTACAMBIO = """ ingrese en que unidad de su eleccion desea que el numero cambie :
K - kilometros
M - metros 
MM - milimetros 
"""
MENSAJEERROR = "el numero ingresano es no valido"

#------entrada del codigo------#
medida = float (input (PREGUNTACENTIMETROS))
unidad = input(PREGUNTACAMBIO)
metros = medida *10**-2
kilometros = medida *10**-5
milimetros = medida *10
if (unidad == "K") :
    print (kilometros)
elif (unidad == "M") :
    print (metros)
elif (unidad == "MM") :
    print (milimetros)
else :
    print (MENSAJEERROR)