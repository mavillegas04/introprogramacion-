#------constantes------#
MENSAJEBIENVENIDA = "bienvenido, vamos a mirar en que estado te encuentras"
MENSAJETRGLICERIDOS = "por favor ingrese el nivel de trigliceridos en el que se encuentra"
MENSAJEHOMOCISTEINA = "por favor ingrese el niverl de homocisteina en el que se encuentra"
MENSAJERESPUESTA = "estas clasificado como {}"
MENSAJEDESPEDIDA = "hasta luego, que tengas un lindo dia"

#------entrada codigo------#
print (MENSAJEBIENVENIDA)
triglicerido = float (input (MENSAJETRGLICERIDOS))
if (triglicerido < 150) :
    print (MENSAJERESPUESTA . format ("optimo, cuidate mucho"))
elif (triglicerido > 150 and triglicerido < 199) :
    print (MENSAJERESPUESTA . format ("sobre el limite optimo, cuidate mucho"))
elif (triglicerido > 200 and triglicerido < 499) :
    print (MENSAJERESPUESTA . format ("alto, tinenes que tener cuidado, cuidate mucho"))
else :
    print (MENSAJERESPUESTA . format ("muy alto, mucho cuidado"))

homocisteina = float (input (MENSAJEHOMOCISTEINA))
if (homocisteina > 2 and homocisteina < 15) :
    print (MENSAJERESPUESTA . format ("optimo, cuidate mucho"))
elif (homocisteina > 15 and homocisteina < 30) :
    print (MENSAJERESPUESTA . format ("sobre el limite optimo, cuidate mucho"))
elif (homocisteina > 30 and homocisteina < 100) :
    print (MENSAJERESPUESTA . format ("alto, mucho cuidado"))
else :
    print (MENSAJERESPUESTA . format ("muy alto, mucho cuidado"))
print (MENSAJEDESPEDIDA)