#-----CONSTANTES-----#
MENSAJEBIENVENIDA = "bienvenido, vamos a comenzar"
NUMEROA = "ingrese un numero A :"
NUMEROB = "ingrese un numero B :"
MENSAJEMAYOR = "el numero {} es mayor que {}"
MENSAJEIGUAL = "el numero {} es igual que {}"

#------ENTRADA CODIGO-----#
print (MENSAJEBIENVENIDA)
NUMEROA = int (input (NUMEROA))
NUMEROB = int (input (NUMEROB))
if (NUMEROA > NUMEROB) :
    print (MENSAJEMAYOR . format ("A","B", NUMEROA, NUMEROB))
elif (NUMEROB > NUMEROA) :
    print (MENSAJEMAYOR . format ("B","A", NUMEROB, NUMEROA)) 
else :
    print (MENSAJEIGUAL . format ("A","B", NUMEROA, NUMEROB))