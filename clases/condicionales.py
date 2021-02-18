#-----constantes-----#
MENSAJE_BIENVENIDA = "hola, espero estes bien"
MENSAJE_MAYOR = "el numero A es mayor que B"
MENSAJE_MENOR = "el numero A es menor que B"
MENSAJE_IGUAL= "A y B son iguales"
PREGUNTA_NUMERO_A = "ingrese un numero A"
PREGUNTA_NUMERO_B = "ingrese un numero B"

#-----entrada codigo-----#
print (MENSAJE_BIENVENIDA)
numeroA = int (input (PREGUNTA_NUMERO_A))
numeroB = int (input (PREGUNTA_NUMERO_B))
ismayor = numeroA > numeroB
ismenor = numeroA < numeroB 

if (ismayor):
    print (MENSAJE_MAYOR)
elif (ismenor):
    print (MENSAJE_MENOR)
else:
    print (MENSAJE_IGUAL)
